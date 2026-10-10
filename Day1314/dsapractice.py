#longest common prefix



def longest_common_prefix(words):
    prefix = ""

    # Check each character of the first word
    for i in range(len(words[0])):

        # Take the current character
        current_char = words[0][i]

        # Compare it with every other word
        for j in range(1, len(words)):

            # Check if the word is too short
            if i >= len(words[j]):
                return prefix

            # Check if characters are different
            if words[j][i] != current_char:
                return prefix

        # If all words have the same character
        prefix = prefix + current_char

    return prefix


words = ["flower", "flow", "flight"]

result = longest_common_prefix(words)

print(result)




#Anagram check


def is_anagram(str1, str2):

    # Step 1: Check the lengths
    if len(str1) != len(str2):
        return False

    # Step 2: Checking every character
    for i in range(len(str1)):

        char = str1[i]

        count1 = 0
        count2 = 0

        # Count character in the first string
        for j in range(len(str1)):
            if str1[j] == char:
                count1 = count1 + 1

        # Count character in the second string
        for j in range(len(str2)):
            if str2[j] == char:
                count2 = count2 + 1

        # Compare the counts
        if count1 != count2:
            return False

    return True


print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("aabb", "abab"))


#Max profit from stock prices

def max_profit(prices):
    if len(prices) == 0:
        return 0

    minimum_price = prices[0]
    maximum_profit = 0

    for i in range(1, len(prices)):
        current_price = prices[i]

        profit = current_price - minimum_price

        if profit > maximum_profit:
            maximum_profit = profit

        if current_price < minimum_price:
            minimum_price = current_price

    return maximum_profit


prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))
