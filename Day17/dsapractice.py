def binary_search(numbers: list[int], target: int) -> int | None:
    """Return the target's index in a sorted list, or None if it is absent."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


def find_missing_number(numbers: list[int]) -> int:
    """Find the missing value from the unique integers 1 through len(numbers)+1."""
    expected_total = (len(numbers) + 1) * (len(numbers) + 2) // 2
    return expected_total - sum(numbers)


if __name__ == "__main__":
    print(binary_search([10, 20, 30, 40, 50, 60, 70], 50))
    print(find_missing_number([1, 2, 4, 5]))
