##### Find the Largest and Second Largest Numbers in a List #####   



numbers = [10, 50, 20, 80, 30]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:

    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest and number != largest:
        second_largest = number

print("Largest:", largest)
print("Second Largest:", second_largest)