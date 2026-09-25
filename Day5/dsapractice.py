###Python Dictionary vs List



#List
numbers = [10, 20, 30, 40]

#Data is stored by position/index.

print(numbers[0])

#Output:10


#Dictionary
student = {
    "name": "Puneet",
    "age": 28
}

#Data is stored using keys.

print(student["name"])

#Output:Puneet



## Missing Number

numbers = [1, 2, 3, 5]

n = 5

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number:", i)


#Missing number: 4



#Two Sum

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])


#Output: 2 7
