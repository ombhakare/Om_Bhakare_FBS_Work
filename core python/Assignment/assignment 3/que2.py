#2.Write a program to input any alphabet and check whether it is vowel or consonant.

# Input from user
alphabet = input("Enter a single alphabet: ")

# Check if input is a single alphabetic character
if len(alphabet) == 1 and alphabet.isalpha():
    # Convert to lowercase for uniform comparison
    alphabet = alphabet.lower()

    # Check if it's a vowel
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet.")