def longest_substring_without_repeating_characters(text: str) -> int:
    """Return the length of the longest substring with no repeated character."""
    last_seen: dict[str, int] = {}
    window_start = 0
    longest = 0

    for index, character in enumerate(text):
        previous_index = last_seen.get(character)
        if previous_index is not None and previous_index >= window_start:
            window_start = previous_index + 1

        last_seen[character] = index
        longest = max(longest, index - window_start + 1)

    return longest


def merge_intervals(
    intervals: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    """Combine overlapping intervals and return them in ascending order."""
    if not intervals:
        return []

    merged: list[tuple[int, int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))

    return merged
