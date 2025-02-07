# Functions in Python

# What is a Function?
"""
A function is a reusable block of code designed to perform a specific task. 
Functions help reduce redundancy, make the code modular, and improve readability.

**Advantages of Functions:**
1. Code Reusability: Write once, use multiple times.
2. Modularity: Break down complex problems into smaller, manageable parts.
3. Improved Readability: Functions provide a logical structure to the code.
4. Easy Maintenance: Changes in functionality can be managed without affecting the entire program.
5. Debugging: Functions isolate errors to specific parts of the code.

**Types of Functions:**
1. Built-in Functions: Predefined functions like `len()`, `type()`, `print()`, etc.
2. User-defined Functions: Functions created by the programmer.
"""

# Example: Built-in Functions
nums = [1, 2, 3, 4, 5]
print("Length of list:", len(nums))
print("Maximum number:", max(nums))
print("Type of nums:", type(nums))

# Defining and Calling Functions
"""
To define a function, use the `def` keyword, followed by the function name and parentheses `()`.
The code block within the function is indented.

Syntax:
def function_name(parameters):
    # Function body
    return result (optional)
"""

# Example: Simple Function
def greet():
    print("Hello, welcome to Python programming!")

# Calling the Function
greet()

# Parameters and Arguments
"""
Parameters are placeholders used in the function definition.
Arguments are actual values passed to the function when it is called.

**Types of Arguments:**
1. Positional Arguments: Passed in the same order as parameters.
2. Keyword Arguments: Passed with parameter names for clarity.
3. Default Arguments: Parameters with default values.
4. Variable-length Arguments: Accept any number of arguments using `*args` (non-keyword) or `**kwargs` (keyword).
"""

# Example: Function with Parameters
def greet_person(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling with Positional Arguments
greet_person("Hussnain", 22)

# Example: Function with Default Arguments
def greet_city(name, city="Depalpur"):
    print(f"Hello {name}, welcome to {city}!")

# Calling Function
greet_city("Ali")  # Uses default value for city
greet_city("Sunny", "Karachi")  # Overrides default value

# Example: Function with Variable-length Arguments
def list_fruits(*fruits):
    print("Fruits:", fruits)

list_fruits("Apple", "Banana", "Cherry")

# Function with Keyword Variable-length Arguments
def person_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

person_details(name="Hussnain", age=22, city="Depalpur", profession="Student")

# Return Values
"""
Functions can return a value using the `return` statement. 
This allows functions to send the computed result back to the caller.
"""

# Example: Function with Return Value
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print("Area of rectangle:", area)

# Lambda Functions
"""
Lambda functions are one-liner anonymous functions. They are defined using the `lambda` keyword 
and can have multiple arguments but only one expression.

Syntax:
lambda arguments: expression
"""

# Example: Lambda Function
square = lambda x: x ** 2
print("Square of 4:", square(4))

# Lambda with Multiple Arguments
add = lambda a, b: a + b
print("Sum of 3 and 5:", add(3, 5))

# Recursive Functions
"""
A recursive function is a function that calls itself to solve smaller subproblems. 
It must have a base case to avoid infinite recursion.

Common use cases: Factorial, Fibonacci series, Tree traversals.
"""

# Example: Recursive Function for Factorial
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Example: Recursive Function for Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib_series = [fibonacci(i) for i in range(10)]
print("Fibonacci Series (10 terms):", fib_series)

# Example Programs Using Functions

# Program 1: Prime Number Checker
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 17
print(f"Is {number} a prime number?", is_prime(number))

# Program 2: Simple Calculator
def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

operation = input("Enter operation (add, subtract, multiply, divide): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
result = calculator(operation, a, b)
print("Result:", result)

# Program 3: Palindrome Checker
def is_palindrome(string):
    return string == string[::-1]

word = "radar"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

# Program 4: Generate Multiplication Table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

number = 5
print(f"Multiplication Table for {number}:")
multiplication_table(number)
