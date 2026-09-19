"""The seed must stay a seed, and the docs must stop contradicting each other.

Every assertion here is a bug that actually happened in this repository.
"""
import glob
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SEED_ID = "myth-campaign-purewater-s1"


def _yaml_field(text, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]+)"?\s*$', text, re.M)
    return m.group(1).strip() if m else None


@pytest.fixture(scope="module")
def manifest():
    return (ROOT / "campaign.yaml").read_text()


def test_the_seed_has_not_been_played(manifest):
    """The root was once a half-played export whose opening scene named a
    specific PC, which meant a fresh install started mid-story."""
    assert _yaml_field(manifest, "id") == SEED_ID
    assert _yaml_field(manifest, "session_number") == "0"
    assert _yaml_field(manifest, "time_index") == "52", "seed must sit at d-3/dawn"

    events = json.loads((ROOT / "journal" / "events.json").read_text())
    assert len(events) == 1, f"a seed carries one seed note, not {len(events)}"
    assert events[0]["type"] == "gm-note"

    beats = glob.glob(str(ROOT / "beats" / "*.md"))
    assert beats, "no beats found"
    for b in beats:
        assert 'status: "pending"' in Path(b).read_text(), f"{Path(b).name} is not pending"


def test_the_opening_scene_names_no_character(manifest):
    """It used to read 'Conall Bjornlasch is riding in beside his patron...'."""
    scene = _yaml_field(manifest, "current_scene") or ""
    for name in ("Conall", "Gardwen", "Magda", "Randall", "Kag"):
        assert name not in scene, f"the seed's opening scene names {name}"
    assert "/purewater:start" in scene, "the scene should stop the GM and point at the command"


def test_kag_is_an_npc_and_not_a_pc():
    """She was the player character for run 4 and is canon now. She ships as an
    NPC so a new party can meet her; if she reappears as a PC the seed is dirty."""
    assert (ROOT / "characters" / "npcs" / "kag.json").exists()
    assert not (ROOT / "characters" / "pcs" / "kag.json").exists()
    kag = json.loads((ROOT / "characters" / "npcs" / "kag.json").read_text())
    assert kag["type"] == "npc"
    assert "Killing is the last resort" not in kag.get("passions", {}), \
        "that passion is earned in play, not shipped"


def test_only_one_campaign_id_is_ever_offered():
    """Three documents once claimed three different live campaign ids, and the
    one CLAUDE.md called 'the live game' was a whole run out of date."""
    shipped = ["campaign.yaml", "README.md", "skills/purewater/SKILL.md",
               "commands/start.md", "scripts/session-start.sh"]
    for rel in shipped:
        f = ROOT / rel
        if not f.exists():
            continue
        found = set(re.findall(r"myth-campaign-[a-z0-9-]+", f.read_text()))
        assert found <= {SEED_ID}, f"{rel} names other campaign ids: {found - {SEED_ID}}"


def test_the_plugin_declares_the_engine_as_a_dependency():
    p = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    assert p["name"] == "purewater"
    assert "mythras-gm" in p.get("dependencies", []), \
        "the campaign cannot run without the engine; say so in the manifest"
    assert (ROOT / "hooks" / "hooks.json").exists()
    assert (ROOT / "scripts" / "engine.sh").exists(), \
        "a plugin cannot resolve a sibling's root, so the resolver is required"


def test_the_start_command_guards_against_resetting_a_live_game():
    """The worst thing this plugin could ship: a returning player types
    /purewater:start and loses their campaign."""
    cmd = (ROOT / "commands" / "start.md").read_text()
    assert "session number above 0" in cmd
    assert "/mythras-gm:play" in cmd, "an in-progress game must be handed to play"
    assert "do not re-seed" in cmd.lower() or "do not import" in cmd.lower()


def test_the_new_player_path_briefs_before_it_asks():
    """Knowing that Passions matter changes what a player writes down, so the
    Mythras briefing has to come before character creation."""
    cmd = (ROOT / "commands" / "start.md").read_text()
    assert "NEW-TO-MYTHRAS.md" in cmd
    i_brief = cmd.index("NEW-TO-MYTHRAS.md")
    i_choose = cmd.index("choosing-a-character.md")
    assert i_brief < i_choose, "brief the player before offering the characters"
    assert "welcome-to-purewater.md" in cmd, "the setting briefing is missing"
    assert "rolling-your-own.md" in cmd, "the roll-your-own path is missing"
    assert "entry-points" in cmd, "the chosen character's backstory is never delivered"


def test_the_player_briefing_keeps_its_secrets():
    """A player-visible file once gave away the twins, the parentage and the
    carving in four bullet points."""
    for f in (ROOT / "lore" / "player-briefing").glob("*.md"):
        text = f.read_text()
        assert 'visibility: "player"' in text, f"{f.name} should be player-visible"
        low = text.lower()
        for spoiler in ("twin", "possess", "baron's son", "soul-knife"):
            assert spoiler not in low, f"{f.name} leaks: {spoiler}"

    companions = ROOT / "lore" / "character-creation" / "the-four-companions.md"
    assert 'visibility: "gm"' in companions.read_text(), \
        "the-four-companions gives away most of two acts and must be GM-only"


def test_the_readme_counts_match_the_disk():
    """The contents table drifted by up to 22 beats."""
    readme = (ROOT / "README.md").read_text()
    for label, pattern in (("Locations", "locations/*.md"),
                           ("Factions", "factions/*.md"),
                           ("Agendas", "agendas/*.md"),
                           ("Beats", "beats/*.md"),
                           ("Facts", "facts/*.md")):
        actual = len(glob.glob(str(ROOT / pattern)))
        m = re.search(rf"\|\s*{label}\s*\|\s*(\d+)", readme)
        assert m, f"README has no {label} row"
        assert int(m.group(1)) == actual, f"README says {label} {m.group(1)}, disk says {actual}"


def test_no_documented_directory_is_missing():
    """README documented an `encounters/` directory that does not exist."""
    readme = (ROOT / "README.md").read_text()
    for d in re.findall(r"\|\s*`([a-z-]+)/`\s*\|", readme):
        assert (ROOT / d).is_dir(), f"README documents {d}/ which does not exist"
