###Reverse a list in Python

numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:

    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)



####maximum number in a list
numbers = [10, 5, 25, 8, 15]

maximum = numbers[0]

for number in numbers:

    if number > maximum:
        maximum = number

print(maximum)



###binary search in a sorted list
numbers = [10, 20, 30, 40, 50, 60, 70]

target = 60

left = 0
right = len(numbers) - 1

while left <= right:

    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Found at index:", middle)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1



###valid parentheses
def is_valid(s):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:

        if char in "([{":
            stack.append(char)

        else:

            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0