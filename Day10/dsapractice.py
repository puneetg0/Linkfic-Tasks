### Dictionary CRUD Operations

student = {
    "name": "Raman",
    "age": 18,
    "course": "Python"
}

# Create
student["city"] = "Delhi"

# Read
print(student["name"])

# Update
student["age"] = 29

# Delete
del student["city"]

print(student)


### Second largest number in a list

numbers = [10, 5, 20, 8, 15]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)


## Merge Sorted Arrays
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

while i < len(arr1):
    result.append(arr1[i])
    i += 1

while j < len(arr2):
    result.append(arr2[j])
    j += 1

print(result)

####Rotate Array to the Right

arr = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    last = arr.pop()

    for i in range(len(arr), 0, -1):
        arr[i - 1] = arr[i - 2] if i > 1 else arr[i - 1]

    arr.insert(0, last)

print(arr)