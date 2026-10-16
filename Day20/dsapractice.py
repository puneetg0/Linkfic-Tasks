# Problem 1: Rotate Array
# Task: Rotate an array to the right by k positions.
# Example:
# Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]


def rotate(nums, k):
    n = len(nums)

    if n == 0:
        return nums

    k = k % n

    nums[:] = nums[-k:] + nums[:-k] if k else nums

    return nums


numbers = [1, 2, 3, 4, 5, 6, 7]
print(rotate(numbers, 3))


# Explanation:
# - n = len(nums) gets the array length.
# - k % n handles rotations larger than the array length.
# - nums[-k:] selects the last k elements.
# - nums[:-k] selects the remaining elements.
# - Combining both parts rotates the array to the right.
# - The if k else nums condition handles zero rotations.
# Time complexity: \(O(n)\). Extra space: \(O(n)\) for the slicing-based solution.


# #Product of Array Except Self

# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


print(product_except_self([1, 2, 3, 4]))



# First pass: store the product of all elements to the left of each index.

# Second pass: multiply each result by the product of all elements to its right.

# No division is used, so the approach also handles arrays containing zeros.

# Time complexity: \(O(n)\).

