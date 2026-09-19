---
id: "myth-lore-4adb6803294a"
title: "GM Guide: Running the Living World"
category: "gm-guide"
visibility: "gm"
summary: "How the agenda/beat engine drives this campaign, and how to bend it"
created_at: "2026-09-05T12:00:00"
---

**GM ONLY.** How this campaign is built, and how to run it.

## There is no plot, there are clocks

The old version of this adventure was a timeline: on this day Santo attacks, on
that day the locket is stolen, then the purge, then the tourney. That works
exactly once, and only if the party stands where the script needs them.

This version is built out of **agendas** and **beats** instead.

- An **agenda** (`agendas/`) is what a character or faction *wants*, with a clock
  measuring how close they are. Santo wants to bind a demon and be seen as his
  father's son. The Baron wants to win the Tourney with a champion nobody has
  looked at. Marisette wants the name of whoever cut her girl.
- A **beat** (`beats/`) is the next concrete thing an agenda produces if nobody
  interferes -- placed in world time (`d-3/night`) or gated on a clock
  (`clock>=4`), with a location and a cast.

The tournament clock still runs from **d-3** (arrival) to **d0** (the Lake Lady's
Tourney), four watches to the day: `dawn`, `day`, `dusk`, `night`.

## The loop

```
list-agendas --campaign C --compact     # what is in motion
tick --campaign C --to "d-3/night"      # move time; see what came due
```

`tick` returns each due beat flagged **onscreen** or **offscreen**. That flag is
not your choice -- it is computed from where the PCs actually are. A beat is
onscreen when a PC is at its location or in its cast.

- **Onscreen** -> play it as a scene.
- **Offscreen** -> it happened anyway. Record it with
  `fire-beat --outcome narrated --log` so it enters the journal as a fact the
  party can *discover*: a rumour, a body, a closed door, a girl who was already
  bleeding when they got there.

This is the whole design. The same beat is a fight, an alibi, or a piece of news
depending only on where the players went.

## Adapt, don't adhere

Every beat file ends with notes on what to do when the players have made the
plan stale. Use them.

- `revise-beat` moves a beat's time, place, cast or framing.
- `add-agenda` mid-session when player action creates a new interest -- someone
  robbed wants restitution, someone saved owes a favour.
- `set-agenda-status --status thwarted` when they genuinely beat something, and
  then let the holder *react*. A thwarted agenda should produce a new one, not a
  quiet re-run of the old.
- `advance-agenda --by N` when the fiction earns it. Clocks are not timers.

The test of a beat is that it would happen without the PCs. If it only makes
sense when they are watching, it is a scene, not a beat -- write it as an
encounter instead.

## The one that fires on being seen

`agendas/hanzo-secures-the-bastard.md` starts **dormant** and activates the
moment the Baron or his people get a clear look at Randall's or Conall's face.
Once active it never goes dormant again and it drives the back half of the
campaign as a pursuit.

This is deliberate: it makes the players' own visibility the thing that raises
the stakes, rather than a GM decision about when to turn up the heat. Let them
walk into it or avoid it, and mean it either way.

## What the players should never be told

The possession scheme, the twins' parentage, and Thuban's nature are in
`lore/gm-secret/`. They come out through play. In particular, do not let Gardwen
learn who the champion is before the reveal at `d0` -- and if the players work it
out early, that is a *better* story, so bring the reveal forward with
`revise-beat` rather than stonewalling them.
