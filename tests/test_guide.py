"""The Games Master's guide stays complete, true to the data, and in house style.

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

CHAPTERS = sorted((ROOT / "guide" / "chapters").glob("*.md"))


class _NoImages:
    """Resolve map directives without resizing a single image."""
    def add(self, src):
        return str(src)


@pytest.fixture(scope="module")
def data():
    return build.load()


@pytest.fixture(scope="module")
def expanded(data):
    return {c.name: build.expand(data, c.read_text(), _NoImages()) for c in CHAPTERS}


def test_chapters_are_in_house_style():
    """The Design Mechanism's terms: Games Master, Non-Player Character,
    characters; never GM, NPC, PC or 'etc'; dice as 3d6, not 3D6."""
    bad = []
    for c in CHAPTERS:
        bad += [f"{c.name}:{line}: {word}" for line, word in violations(c.read_text())]
    assert not bad, "house-style breaches:\n" + "\n".join(bad)


def test_headings_stop_at_four():
    for c in CHAPTERS:
        deep = [l for l in c.read_text().splitlines() if re.match(r"#{5,}\s", l)]
        assert not deep, f"{c.name} uses headings deeper than 4: {deep}"


def test_every_directive_resolves(expanded):
    """A directive naming a sheet, beat, map or file that does not exist fails
    the build; this is the same failure, earlier."""
    assert len(expanded) == len(CHAPTERS)


def test_every_beat_has_a_scene(data):
    """Every beat in the catalogue is a scene in the Events chapters, once."""
    found = []
    for c in CHAPTERS:
        found += re.findall(r"<!--\s*beat:\s*([\w-]+)\s*-->", c.read_text())
    missing = set(data["beats"]) - set(found)
    dupes = {b for b in found if found.count(b) > 1}
    assert not missing, f"beats with no scene in the guide: {sorted(missing)}"
    assert not dupes, f"beats with more than one scene: {sorted(dupes)}"


def test_every_character_has_a_stat_block(data, expanded):
    """Full Mythras statistics for everybody: every Non-Player Character,
    every pregenerated character, creature and troop template."""
    text = "\n".join(expanded.values())
    missing = [s["name"] for s in data["sheets"].values() if f"#### {s['name']}\n" not in text]
    assert not missing, f"no stat block for: {missing}"


def test_every_map_sheet_is_in_the_guide():
    text = "\n".join(c.read_text() for c in CHAPTERS)
    for kind in ("districts", "buildings"):
        for d in sorted((ROOT / "maps" / kind).iterdir()):
            if d.is_dir():
                assert f"<!-- map: {kind}/{d.name} -->" in text, f"maps/{kind}/{d.name} is not in the guide"
