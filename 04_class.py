# 😊 Data Types and Variables

# -------------------------------
# What are Variables?
# -------------------------------
# Variables are containers for storing data values. 
# A variable is created when you assign a value to it.
# Example: x = 10

# Defining variables
name = "Sunny"         # String: Textual data
age = 25               # Integer: Whole number
height = 5.9           # Float: Decimal number
is_student = True      # Boolean: True/False value

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# -------------------------------
# What are Data Types?
# -------------------------------
# Data types specify the type of data a variable can hold.
# Python provides built-in data types, which are classified as follows:

# Mutable Data Types:
# list
# dict
# set

# Immutable Data Types:

# str
# tuple
# int
# float
# bool

# -------------------------------
# 1. Numeric Types
# -------------------------------
# Numeric types include `int`, `float`, and `complex`.
# - int: Integer numbers, e.g., -10, 0, 25.
# - float: Decimal numbers, e.g., 3.14, -2.5.
# - complex: Numbers with a real and imaginary part, e.g., 3 + 4j.

# Examples of numeric types
a = 10                  # Integer
b = 3.14                # Float
c = 3 + 4j              # Complex number

print("\nNumeric Data Types:")
print("Integer:", a)
print("Float:", b)
print("Complex:", c)

# -------------------------------
# 2. Text Type: `str`
# -------------------------------
# A `str` holds a sequence of characters (text).
# Strings are defined using single, double, or triple quotes.

# Example of a string
greeting = "Hello, Python!"
print("\nString Example:", greeting)

# -------------------------------
# 3. Sequence Types: `list`, `tuple`
# -------------------------------
# - List: A mutable (modifiable) collection of items.
# - Tuple: An immutable (non-modifiable) collection of items.

# Example of a list
fruits = ["apple", "banana", "cherry"]
print("\nList Example:", fruits)

# Example of a tuple
colors = ("red", "green", "blue")
print("Tuple Example:", colors)

# -------------------------------
# 4. Mapping Type: `dict`
# -------------------------------
# A dictionary stores data as key-value pairs. It is mutable.

# Example of a dictionary
person = {"name": "Sunny", "age": 25, "is_student": True}
print("\nDictionary Example:", person)

# -------------------------------
# 5. Boolean Type: `bool`
# -------------------------------
# Boolean values represent True or False.

# Example of boolean
is_raining = False
print("\nBoolean Example:", is_raining)

# -------------------------------
# 6. Set Types: `set`, `frozenset`
# -------------------------------
# - Set: A collection of unique, unordered items.
# - Frozenset: Immutable version of a set.

# Example of a set
unique_numbers = {1, 2, 3, 3, 2, 1}
print("\nSet Example (unique elements):", unique_numbers)

# -------------------------------
# Type Checking
# -------------------------------
# Use the `type()` function to check the data type of a variable.

print("\nChecking Data Types:")
print("Type of a:", type(a))
print("Type of greeting:", type(greeting))
print("Type of fruits:", type(fruits))
print("Type of person:", type(person))

# -------------------------------
# Dynamic Typing in Python
# -------------------------------
# Python allows dynamic typing, which means a variable can change its data type.

x = 10  # Initially, x is an integer
print("\nInitially, x is:", x, "and its type is:", type(x))

x = "Now I am a string!"  # Now, x is a string
print("Now, x is:", x, "and its type is:", type(x))

# -------------------------------
# Data Type Operations
# -------------------------------

# Example 1: Adding two numbers
num1 = 7
num2 = 3
print("\nSum of", num1, "and", num2, "is:", num1 + num2)

# Example 2: Concatenating strings
first_name = "Sunny"
last_name = "Khan"
print("Full Name:", first_name + " " + last_name)

# Example 3: Working with lists
fruits.append("orange")  # Add an item to the list
print("Updated Fruits List:", fruits)

# Example 4: Dictionary Operations
person["city"] = "Lahore"  # Add a new key-value pair
print("Updated Dictionary:", person)

# Example 5: Boolean logic
is_sunny = True
is_windy = False
print("\nIs it sunny and windy?", is_sunny and is_windy)

# Example 6: Using Sets
another_set = {3, 4, 5}
print("Union of sets:", unique_numbers.union(another_set))

# ================================
# End of Data Types and Variables
# ================================
