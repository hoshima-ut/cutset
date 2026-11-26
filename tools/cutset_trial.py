"""Build a read-only audition plan for the public 25 fps interview pilot."""

import argparse
import json
from pathlib import Path
import sys

REFERENCE = Path(__file__).with_name("fixtures") / "interview-layout.json"
CANDIDATES = {"A": (205, 245), "B": (505, 565), "C": (800, 825)}
ITEM_KEYS = ("clip", "item", "link", "startFrame", "endFrame", "sourceIn",
             "sourceOut", "name", "speed", "reverse", "enabled")
TRACK_KEYS = ("id", "locked", "enabled", "syncLock", "muted", "solo")


def layout(sequence):
    """Select only the timing, identities and track state used by the pilot."""
    result = {"name": sequence["name"], "id": sequence["id"],
              "durationFrames": sequence["durationFrames"],
              "settings": {"frame_rate": sequence["settings"]["frame_rate"]}}
    for kind in ("audio", "video"):
        result[kind] = []
        for track in sequence[kind]:
            row = {key: track[key] for key in TRACK_KEYS}
            row["items"] = [{key: clip[key] for key in ITEM_KEYS} for clip in track["items"]]
            result[kind].append(row)
    return result


def plan(sequence, cuts):
    # Compare canonical JSON so e.g. true cannot stand in for the integer 1.
    observed = layout(sequence)
    expected = json.loads(REFERENCE.read_text(encoding="utf-8"))
    if json.dumps(observed, sort_keys=True) != json.dumps(expected, sort_keys=True):
        raise ValueError("sequence timing, identity or track state differs from the pilot")
    if not set(cuts) <= CANDIDATES.keys():
        raise ValueError("unknown candidate")
    removed = 0
    decisions = []
    for name, (start, end) in CANDIDATES.items():
        cut = name in cuts
        target = start - removed
        # Audition spans reference source frames; a cut joins the two outer handles.
        handles = [[start - 25, start], [end, end + 25]]
        decisions.append({"id": name, "decision": "cut" if cut else "keep",
                          "source": [start, end], "result": [target, target if cut else end - removed],
                          "originalAudition": [[start - 25, end + 25]],
                          "proposedAudition": handles if cut else [[start - 25, end + 25]]})
        if cut:
            removed += end - start
    # Locked music can outlast the shortened editable tracks.
    picture_end = sequence["durationFrames"] - removed
    music = observed["audio"][2]
    return {"profile": "interview-pilot-v1", "sequence": observed["id"], "fps": 25,
            "lockedTrack": music["id"], "targetClips": [observed["video"][0]["items"][0]["clip"],
                                                        observed["audio"][0]["items"][0]["clip"]],
            "pictureEnd": picture_end, "sequenceEnd": max(picture_end, music["items"][0]["endFrame"]),
            "candidates": decisions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inspect", required=True, type=Path, help="filmcraft-cli inspect sequence JSON")
    parser.add_argument("--cut", nargs="*", choices=list(CANDIDATES), default=["A", "B"])
    args = parser.parse_args()
    try:
        sequence = json.loads(args.inspect.read_text(encoding="utf-8"))
        result = plan(sequence, args.cut)
    except (OSError, KeyError, TypeError, ValueError) as error:
        parser.exit(2, f"Cannot preview this pilot: {error}\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
