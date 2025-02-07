# 😊 Comments and inputs in python

# This is a single-line comment

----------------------------------------------------------------

"""
This is a multi-line comment.
Used for documentation or commenting out multiple lines.
"""
----------------------------------------------------------------
"""
This is a multi-line comment.
Used for documentation or commenting out multiple lines.
"""

# Example of using comments in code
# A simple addition program
num1 = 5  # First number
num2 = 10  # Second number
result = num1 + num2  # Add numbers
print("The result of addition is:", result)

# ---------------------------
# Input and Output Functions
# ---------------------------

# Input from user and print their name
name = input("What is your name? ")  # Input function to get user's name
print(f"Hello, {name}!")  # Output the name using f-string

# Example of a basic calculator using input() and print()
print("\nBasic Calculator")
num1 = float(input("Enter the first number: "))  # Get first number
num2 = float(input("Enter the second number: "))  # Get second number
operation = input("Enter operation (+, -, *, /): ")  # Get operation

if operation == "+":
    print(f"The sum is: {num1 + num2}")
elif operation == "-":
    print(f"The difference is: {num1 - num2}")
elif operation == "*":
    print(f"The product is: {num1 * num2}")
elif operation == "/":
    if num2 != 0:  # Avoid division by zero
        print(f"The quotient is: {num1 / num2}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation.")