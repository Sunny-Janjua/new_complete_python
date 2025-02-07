# Python Control Statements

# Control statements allow you to control the flow of execution in a program. 
# There are three main types of control statements in Python:
# 1. Conditional Statements (if, elif, else)
# 2. Looping Statements (for, while)
# 3. Control Flow Modification (break, continue, pass)

# ---------------------------------------------------------
# 1. Conditional Statements
# Conditional statements allow the execution of certain code only if a condition is true.

# if statement
age = 20
if age >= 18:
    print("You are eligible to vote!")  # Output: You are eligible to vote!

# if-else statement
age = 16
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")  # Output: You are not eligible to vote!

# if-elif-else statement
day = "Sunday"
if day == "Monday":
    print("Start of the work week.")
elif day == "Friday":
    print("End of the work week.")
else:
    print("It's a weekend or another day.")  # Output: It's a weekend or another day.

# ---------------------------------------------------------
# 2. Looping Statements
# Loops allow the execution of a block of code multiple times.

# for loop (used for iterating over a sequence like list, tuple, etc.)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# for loop with range
for i in range(1, 5):
    print(i)
# Output:
# 1
# 2
# 3
# 4

# while loop (executes as long as the condition is true)
count = 0
while count < 3:
    print("Count is:", count)  # Output: Count is: 0, Count is: 1, Count is: 2
    count += 1

# ---------------------------------------------------------
# 3. Control Flow Modification
# These statements are used to alter the flow of a loop or a conditional block.

# break statement (exits the loop)
for num in range(1, 10):
    if num == 5:
        break  # Exits the loop when num equals 5
    print(num)  # Output: 1, 2, 3, 4

# continue statement (skips the current iteration and moves to the next one)
for num in range(1, 6):
    if num == 3:
        continue  # Skips the print statement when num equals 3
    print(num)  # Output: 1, 2, 4, 5

# pass statement (used as a placeholder for code that hasn't been written yet)
def some_function():
    pass  # Function does nothing, just a placeholder

# ---------------------------------------------------------
# Nested Conditional Statements
# You can also nest if statements inside other if statements.

x = 10
y = 20

if x == 10:
    if y == 20:
        print("Both x and y are correct.")  # Output: Both x and y are correct.

# Nested Loops
# You can also nest loops (a loop inside another loop).

for i in range(1, 3):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")
# Output:
# i = 1, j = 1
# i = 1, j = 2
# i = 2, j = 1
# i = 2, j = 2

# ---------------------------------------------------------
# Example Summary

# 1. Using if-else to check for even/odd numbers
number = 15
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")  # Output: 15 is odd.

# 2. Using for loop to iterate over a string
name = "Python"
for letter in name:
    print(letter)
# Output:
# P
# y
# t
# h
# o
# n

# 3. Using while loop to count down
count = 5
while count > 0:
    print(count)
    count -= 1
# Output:
# 5
# 4
# 3
# 2
# 1
