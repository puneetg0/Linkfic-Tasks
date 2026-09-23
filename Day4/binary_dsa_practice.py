# ////// DSA / Coding Practice
# 1. Prime Number
# A prime number is divisible only by:
# 1 and itself



# num = int(input("Enter number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")



####Binary Search

#Binary search works on a sorted list.

num=[10, 20, 30, 40, 50, 60, 70, 80, 90]

Target =int(input("Enter number to search: "))

for i in range(len(num)):
    low = 0
    high = len(num) - 1
    mid = (low + high) // 2

    if num[mid] == Target:
        print("Found")
        break
    elif num[mid] < Target:
        low = mid + 1
    else:
        high = mid - 1

    if low > high:
        print("Not Found")
        break