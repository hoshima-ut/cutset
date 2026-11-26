"""Frame-level regression cases for the read-only pilot."""
import copy
import json
import unittest

from cutset_trial import REFERENCE, plan


class PilotPreview(unittest.TestCase):
    def setUp(self):
        self.sequence = json.loads(REFERENCE.read_text())

    def test_default_edit_and_preserved_breath(self):
        before = copy.deepcopy(self.sequence)
        view = plan(self.sequence, ["A", "B"])
        self.assertEqual(view["sequenceEnd"], 1500)
        a, b, c = view["candidates"]
        self.assertEqual(a["proposedAudition"], [[180, 205], [245, 270]])
        self.assertEqual(b["result"], [465, 465])
        self.assertEqual(c["result"], [700, 725])
        self.assertEqual(c["proposedAudition"], c["originalAudition"])
        self.assertEqual(self.sequence, before)

    def test_choices_and_locked_music_tail(self):
        self.assertEqual(plan(self.sequence, [])["sequenceEnd"], 1600)
        full = plan(self.sequence, ["A", "B", "C"])
        self.assertEqual((full["pictureEnd"], full["sequenceEnd"]), (1475, 1500))
        self.assertEqual(plan(self.sequence, ["B"])["candidates"][2]["result"], [740, 765])

    def test_stale_state(self):
        for field, value in (("locked", True), ("id", 99)):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.sequence)
                changed["video"][0][field] = value
                with self.assertRaises(ValueError):
                    plan(changed, [])

    def test_other_rate_and_unknown_candidate(self):
        with self.assertRaises(ValueError):
            plan(self.sequence, ["D"])
        self.sequence["settings"]["frame_rate"]["num"] = 30
        with self.assertRaises(ValueError):
            plan(self.sequence, [])


if __name__ == "__main__":
    unittest.main()
