#7.Find the sum of three-digit number??

number = int(input("Enter a three-digit number: "))


if (number <= 999):

    
    hundreds = number // 100
    
    tens = (number // 10) % 10
    
    units = number % 10
    
    # Calculate sum of digits
digit_sum = hundreds + tens + units

    # Output
print(f"Sum of digits of {number} is: {digit_sum}")
