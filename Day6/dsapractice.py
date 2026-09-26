# This code reverses a list of numbers using a for loop and the range function.


numbers = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)



# This code finds the maximum number in a list using a for loop and an if statement.
numbers = [10, 25, 7, 40, 15]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)

# This code removes duplicates from a list using a for loop and an if statement.

numbers = [1, 2, 2, 3, 3, 4]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)



# This code merges two sorted lists into a single sorted list using a while loop and if statements.


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

result = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):

    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

print(result)