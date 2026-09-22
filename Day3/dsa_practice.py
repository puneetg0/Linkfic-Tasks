### Factorial


def factorial(n):
    result =1

    for i in range(1, n+1):
        result =result * i
    return result

print(f"This is factorial of 5: {factorial(5)}")


##### Fibonacci Series


a = 0
b =1
for i in range(10):
    print(a)
    next=a+b
    a=b
    b=next


####### Find Duplicates

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print(f"Duplicates in the list: {duplicates}")