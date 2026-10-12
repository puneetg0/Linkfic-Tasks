def two_sum(numbers: list[int], target: int) -> list[int] | None:
    previous_indexes: dict[int, int] = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in previous_indexes:
            return [previous_indexes[needed], index]
        previous_indexes[number] = index
    return None


def longest_common_prefix(words: list[str]) -> str:
    if not words:
        return ""

    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([1, 2, 3], 10) is None
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    print("Two Sum and Longest Common Prefix examples passed.")
