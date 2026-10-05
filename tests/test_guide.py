"""Purewater's two books stay complete, true to the data, in house style, and --
for the Players' Guide -- free of spoilers.

Run with: uv run --with pytest --with pyyaml --with pillow pytest -q tests/
"""
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "guide"))

yaml = pytest.importorskip("yaml")
build = pytest.importorskip("build")
from house import violations  # noqa: E402

GM = sorted((ROOT / "guide" / "gm").glob("*.md"))
PLAYERS = sorted((ROOT / "guide" / "players").glob("*.md"))
ALL = GM + PLAYERS


class _NoImages:
    """Resolve map directives without resizing a single image."""
    def add(self, src):
        return str(src)


@pytest.fixture(scope="module")
def data():
    return build.load()


@pytest.fixture(scope="module")
def expanded(data):
    return {c: build.expand(data, c.read_text(), _NoImages()) for c in ALL}


def test_both_books_exist():
    assert GM, "no Games Master's Guide chapters"
    assert PLAYERS, "no Players' Guide chapters"


def test_chapters_are_in_house_style():
    """The Design Mechanism's terms: Games Master, Non-Player Character,
    characters; never GM, NPC, PC or 'etc'; dice as 3d6, not 3D6."""
    bad = []
    for c in ALL:
        bad += [f"{c.parent.name}/{c.name}:{line}: {word}" for line, word in violations(c.read_text())]
    assert not bad, "house-style breaches:\n" + "\n".join(bad)


def test_every_chapter_has_a_part_and_a_title():
    for c in ALL:
        text = c.read_text()
        assert re.search(r"^<!--\s*part:\s*.+-->", text, re.M), f"{c.name} has no <!-- part: --> line"
        assert re.search(r"^#\s+\S", text, re.M), f"{c.name} has no title"


def test_headings_stop_at_four():
    for c in ALL:
        deep = [l for l in c.read_text().splitlines() if re.match(r"#{5,}\s", l)]
        assert not deep, f"{c.name} uses headings deeper than 4: {deep}"


def test_every_directive_resolves(expanded):
    assert len(expanded) == len(ALL)


def test_every_beat_is_told_once(data):
    """The Games Master's Guide is prose, not a list of beats -- but every beat in
    the catalogue is told somewhere in it, exactly once, and says so with a
    <!-- covers: --> marker beside the prose that tells it."""
    told = []
    for c in GM:
        for m in re.finditer(r"<!--\s*covers:\s*(.*?)\s*-->", c.read_text()):
            told += [s.strip() for s in m.group(1).split(",") if s.strip()]
    missing = set(data["beats"]) - set(told)
    dupes = {b for b in told if told.count(b) > 1}
    assert not missing, f"beats the guide never tells: {sorted(missing)}"
    assert not dupes, f"beats told more than once: {sorted(dupes)}"


def test_every_sheet_has_a_stat_block(data, expanded):
    """Full Mythras statistics for everybody, in the Games Master's Guide."""
    text = "\n".join(v for k, v in expanded.items() if k in GM)
    missing = [s["name"] for s in data["sheets"].values() if f"#### {s['name']}\n" not in text]
    assert not missing, f"no stat block for: {missing}"


def test_every_map_sheet_is_in_the_gm_guide():
    text = "\n".join(c.read_text() for c in GM)
    for kind in ("districts", "buildings"):
        for d in sorted((ROOT / "maps" / kind).iterdir()):
            if d.is_dir():
                assert f"<!-- map: {kind}/{d.name} -->" in text, f"maps/{kind}/{d.name} is not in the GM's guide"


SPOILERS = [
    r"\btwins?\b", r"possess", r"Thuban", r"Cailan", r"Gabriel", r"locket", r"\bbinding\b", r"seat(ed|ing)? (a|the) ",
    r"Santo", r"Emmeralda", r"lust spirit", r"the Movement\b", r"Awake the Dragon", r"Asmodeus", r"soul-knife", r"catacomb",
    r"son of (the )?Baron", r"Baron's son", r"Prince'?s? body", r"Dragon King(s)? (reborn|again)",
    r"Sinnit", r"Orrin", r"Ember Society", r"Hesper", r"Quiet Hand",
]


def test_the_players_guide_keeps_the_secrets(data, expanded):
    """A player may read every word of the Players' Guide. Nothing in it may
    give away the possession, the twins, the inciting crime or the endings."""
    bad = []
    for c in PLAYERS:
        text = expanded[c]
        for pat in SPOILERS:
            for m in re.finditer(pat, text, re.I):
                line = text.count("\n", 0, m.start()) + 1
                bad.append(f"players/{c.name}:{line}: {m.group(0)}")
    assert not bad, "the Players' Guide leaks:\n" + "\n".join(bad)


def test_the_players_guide_shows_no_secret_maps():
    for c in PLAYERS:
        for m in re.finditer(r"<!--\s*map:\s*(.*?)\s*-->", c.read_text()):
            assert not m.group(1).startswith(("secrets/", "encounters/")), \
                f"players/{c.name} shows a Games Master's map: {m.group(1)}"
