# Python Operators

# Operators are special symbols used to perform operations on variables and values. 
# Python has various types of operators, including:
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators

# ---------------------------------------------------------
# 1. Arithmetic Operators
# These operators are used to perform basic arithmetic operations.

num1 = 10
num2 = 5

# Addition
print("Addition:", num1 + num2)  # Output: 15

# Subtraction
print("Subtraction:", num1 - num2)  # Output: 5

# Multiplication
print("Multiplication:", num1 * num2)  # Output: 50

# Division (float)
print("Division:", num1 / num2)  # Output: 2.0

# Floor Division (int result)
print("Floor Division:", num1 // num2)  # Output: 2

# Modulus (remainder of division)
print("Modulus:", num1 % num2)  # Output: 0

# Exponentiation (power)
print("Exponentiation:", num1 ** num2)  # Output: 100000

# ---------------------------------------------------------
# 2. Assignment Operators
# These operators are used to assign values to variables.

num = 5

# Assigning value
num = 10  # num is now 10
print("Assignment:", num)  # Output: 10

# Add and assign (num = num + 5)
num += 5
print("Add and Assign:", num)  # Output: 15

# Subtract and assign (num = num - 5)
num -= 5
print("Subtract and Assign:", num)  # Output: 10

# Multiply and assign (num = num * 5)
num *= 5
print("Multiply and Assign:", num)  # Output: 50

# Divide and assign (num = num / 5)
num /= 5
print("Divide and Assign:", num)  # Output: 10.0

# ---------------------------------------------------------
# 3. Comparison Operators
# These operators are used to compare two values.

# Equal to
print("Equal to:", num1 == num2)  # Output: False

# Not equal to
print("Not equal to:", num1 != num2)  # Output: True

# Greater than
print("Greater than:", num1 > num2)  # Output: True

# Less than
print("Less than:", num1 < num2)  # Output: False

# Greater than or equal to
print("Greater than or equal to:", num1 >= num2)  # Output: True

# Less than or equal to
print("Less than or equal to:", num1 <= num2)  # Output: False

# ---------------------------------------------------------
# 4. Logical Operators
# These operators are used to perform logical operations, combining boolean expressions.

# and (both conditions must be true)
print("Logical AND:", (num1 > num2) and (num2 < 10))  # Output: True

# or (at least one condition must be true)
print("Logical OR:", (num1 > num2) or (num2 > 10))  # Output: True

# not (inverts the condition)
print("Logical NOT:", not (num1 > num2))  # Output: False
