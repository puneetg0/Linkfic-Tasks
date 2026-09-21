    #Count vowels in a string

def count_vowels(text):

    #name="Puneet Goswami"

    count =0

    vowels = "aeiouAEIOU"

    for char in text.lower():
        if char in vowels:
            count=count+1

    return count
text = input("Enter a string: ")
print("Number of vowels in the string:",count_vowels(text))




