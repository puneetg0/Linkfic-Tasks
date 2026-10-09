def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for num in numbers:
        actual_sum += num

    missing_number = expected_sum - actual_sum

    return missing_number


numbers = [1, 2, 4, 5]
n = 5

result = find_missing_number(numbers, n)
print(result)

# Explanation

# The numbers should be from 1 to 5.

# Calculate the expected sum using n * (n + 1) // 2. The result is 15.

# Use a for loop to add the numbers in the list. The actual sum is 12.

# Subtract the actual sum from the expected sum: 15 - 12 = 3.

# Return the missing number.

# Output

#3

#Time Complexity


##Maximum Subarray

def max_subarray(numbers):
    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for i in range(1, len(numbers)):
        current_sum = max(
            numbers[i],
            current_sum + numbers[i]
        )

        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray(numbers)
print(result)

# Explanation

# Start with the first number as both the current sum and maximum sum.

# Use a for loop to visit each remaining number.

# Decide whether to start a new subarray at the current number or add it to the previous subarray.

# Update the maximum sum whenever the current sum becomes larger.

# Return the maximum sum at the end.

# The max() function compares two values and returns the larger one.

# Output 6