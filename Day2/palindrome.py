def is_palindrome(text):
    text =text.lower()

    left=0
    right=len(text)-1

    while left<right:

        if text[left] != text[right]:

            return "not palindrome"
            
        left=left+1

        right=right-1

    return "is palindrome"

 #--- Testing the code ---
print(is_palindrome("nayan"))     # Output: is palindrome
print(is_palindrome("hello"))     # Output: not palindrome
print(is_palindrome("race car"))  # Output: is palindrome


text = input("Enter a string: ")
print("The string is:",is_palindrome(text))

