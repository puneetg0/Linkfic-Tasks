import unittest

from Day21.dsapractice import (
    longest_substring_without_repeating_characters,
    merge_intervals,
)


class LongestSubstringTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_substring_without_repeating_characters("abcabcbb"), 3)
        self.assertEqual(longest_substring_without_repeating_characters("bbbbb"), 1)
        self.assertEqual(longest_substring_without_repeating_characters("pwwkew"), 3)

    def test_empty_and_unique_strings(self):
        self.assertEqual(longest_substring_without_repeating_characters(""), 0)
        self.assertEqual(longest_substring_without_repeating_characters("abcdef"), 6)

    def test_repeat_inside_current_window(self):
        self.assertEqual(longest_substring_without_repeating_characters("abba"), 2)


class MergeIntervalsTests(unittest.TestCase):
    def test_merges_overlapping_and_nested_intervals(self):
        self.assertEqual(
            merge_intervals([(1, 3), (2, 6), (8, 10), (9, 12), (2, 4)]),
            [(1, 6), (8, 12)],
        )

    def test_handles_empty_single_and_touching_intervals(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([(3, 5)]), [(3, 5)])
        self.assertEqual(merge_intervals([(1, 2), (2, 4)]), [(1, 4)])


if __name__ == "__main__":
    unittest.main()
