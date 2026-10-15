"""
Day 19 – DSA Practice
Topic: Kadane's Algorithm / Maximum Subarray

─────────────────────────────────────────────────────────────
PROBLEM STATEMENT
─────────────────────────────────────────────────────────────
Given an integer array `nums`, find the subarray with the
largest sum and return that sum.

Example:
  Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  Output: 6
  Why:    The subarray [4, -1, 2, 1] has the largest sum = 6

─────────────────────────────────────────────────────────────
KEY INSIGHT — Kadane's Algorithm
─────────────────────────────────────────────────────────────
At every index, we make one decision:
  "Should I extend the current subarray, or start fresh?"

  current_sum = max(num, current_sum + num)

If adding `num` to the running total is worse than just
starting over at `num`, we start a new subarray.

We track the best running total seen so far as `max_sum`.

Time Complexity:  O(n)  — one pass through the array
Space Complexity: O(1)  — only two variables needed
─────────────────────────────────────────────────────────────
"""


def max_subarray(nums: list[int]) -> int:
    """Return the maximum subarray sum using Kadane's Algorithm."""
    if not nums:
        raise ValueError("Input array must not be empty.")

    current_sum = nums[0]   # Best sum ending at the current position
    max_sum = nums[0]       # Best sum seen so far (the answer)

    # Start from index 1 — we already seeded with index 0
    for num in nums[1:]:
        # Decision: extend current subarray OR start fresh at `num`
        current_sum = max(num, current_sum + num)

        # Update overall best if we found a new maximum
        max_sum = max(max_sum, current_sum)

    return max_sum


# ─────────────────────────────────────────────────────────────
# BONUS: Return the actual subarray, not just the sum
# ─────────────────────────────────────────────────────────────
def max_subarray_with_indices(nums: list[int]) -> tuple[int, list[int]]:
    """
    Returns (max_sum, subarray) — the maximum sum AND the elements.
    Tracks start/end indices during the Kadane pass.
    """
    if not nums:
        raise ValueError("Input array must not be empty.")

    current_sum = nums[0]
    max_sum = nums[0]

    start = 0           # Start of current subarray being tested
    best_start = 0      # Start of the best subarray found
    best_end = 0        # End   of the best subarray found

    for i in range(1, len(nums)):
        # If starting fresh is better, reset start pointer
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start = i
        else:
            current_sum += nums[i]

        # Record best window
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return max_sum, nums[best_start : best_end + 1]


# ─────────────────────────────────────────────────────────────
# Test cases
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        # (input, expected_sum)
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),    # classic example
        ([1],                                       1),    # single element
        ([-1, -2, -3, -4],                         -1),   # all negatives → pick least bad
        ([5, 4, -1, 7, 8],                          23),   # all contribute
        ([0, 0, 0],                                  0),   # zeros
        ([-2, -3, 4, -1, -2, 1, 5, -3],             7),   # [4,-1,-2,1,5]
    ]

    print("=" * 50)
    print("Kadane's Algorithm — Max Subarray Tests")
    print("=" * 50)

    all_passed = True
    for nums, expected in test_cases:
        result = max_subarray(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result != expected:
            all_passed = False
        print(f"{status}  Input: {nums}")
        print(f"        Expected: {expected}  Got: {result}")

        best_sum, subarray = max_subarray_with_indices(nums)
        print(f"        Subarray: {subarray}  (sum={best_sum})")
        print()

    print("All tests passed!" if all_passed else "Some tests FAILED.")
