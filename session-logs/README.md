# Session logs

Ground-truth transcripts for the played campaign, and the extraction used to
rebuild the journal from them.

| File | What it is |
|---|---|
| `session-01-magda-5619508f.jsonl` | The raw Claude Code session log for Session 1 (Gully playing Magda, ford to the Moist Oyster). 4,164 records. |
| `transcript.md` | User/assistant turns only, flattened. 702 turns, 86,245 words. |
| `user_prompts.md` | Every player prompt, verbatim. 261 prompts, 6,381 words. |
| `play_actions.md` | The play spine — the 229 in-character prompts, starting at index 32. |
| `beats_part1.py` … `beats_part3.py` | The 184 beat-level journal events extracted from the transcript, with their real play timestamps. |
| `load_beats.py` | Loads them into TypeDB via `mythras_gm.cmd_log_event(--at ...)`. |

## Why

The session was originally journalled as 13 chapter summaries. That is enough
to resume play and not nearly enough to write from: it compressed whole scenes
to a clause. The body-disposal argument in Constantine's skiff — never-found is
harder than it sounds in a city that dredges itself, then burn-in-a-guild-furnace
versus the deep channel on a ninety-minute ebb, then Magda's pigs — came out as
nine words.

These 184 events restore the beats: the choices, the failed rolls that changed
the shape of a scene, the NPC lines that turned the plot, and the moments the
player found something the GM had missed. They interleave with the original
chapter summaries in true play order, so `get-log` reads as a chronology rather
than a digest.

Re-running `load_beats.py` against a fresh campaign would duplicate them. It is
kept as provenance, not as a fixture.
