#10. Write a program to reverse three-digit number.

number = int(input("Enter a three-digit number: "))


if (number <= 999):

    
    units = number % 10
    
    tens = (number // 10) % 10

    hundreds = number // 100
    
    # Output
print(f"reverse the digit {units}{tens}{hundreds}.")
