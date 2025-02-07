# Typecasting in Python

# Typecasting refers to converting one data type to another. 
# There are two types of typecasting in Python:
# 1. Implicit Typecasting (Automatic type conversion)
# 2. Explicit Typecasting (Manual type conversion)

# ---------------------------------------------------------
# 1. Implicit Typecasting (Automatic Conversion)

# Python automatically converts one data type to another if it is necessary, 
# such as when performing arithmetic operations between different types.

# Example of Implicit Typecasting
num_int = 5           # Integer data type
num_float = 2.5       # Float data type

# Python automatically converts num_int (int) to float for the operation
result = num_int + num_float  # The result will be a float
print("Result of Implicit Typecasting:", result)  # Output: 7.5

# ---------------------------------------------------------
# 2. Explicit Typecasting (Manual Conversion)

# You can manually convert (cast) a variable from one data type to another 
# using built-in functions. Common typecasting functions in Python include:
# - int()    : Converts to an integer
# - float()  : Converts to a float
# - str()    : Converts to a string
# - list()   : Converts to a list
# - tuple()  : Converts to a tuple
# - set()    : Converts to a set

# ---------------------------------------------------------
# Examples of Explicit Typecasting

# 1. Converting float to int
num_float = 3.14
num_int = int(num_float)  # Convert float to int (decimal part will be truncated)
print("Float to Int:", num_int)  # Output: 3

# 2. Converting int to float
num_int = 5
num_float = float(num_int)  # Convert int to float
print("Int to Float:", num_float)  # Output: 5.0

# 3. Converting int to string
num_int = 10
num_str = str(num_int)  # Convert int to string
print("Int to String:", num_str)  # Output: '10'

# 4. Converting string to int
num_str = "100"
num_int = int(num_str)  # Convert string to int
print("String to Int:", num_int)  # Output: 100

# 5. Converting string to float
num_str = "3.14"
num_float = float(num_str)  # Convert string to float
print("String to Float:", num_float)  # Output: 3.14

# 6. Converting a string to a list
str_value = "hello"
list_value = list(str_value)  # Convert string to list
print("String to List:", list_value)  # Output: ['h', 'e', 'l', 'l', 'o']

# ---------------------------------------------------------
# Summary of Common Typecasting Functions

# 1. int()    - Converts to an integer
# 2. float()  - Converts to a float
# 3. str()    - Converts to a string
# 4. list()   - Converts to a list
# 5. tuple()  - Converts to a tuple
# 6. set()    - Converts to a set

# ---------------------------------------------------------
# Example Summary:

# 1. Converting a float to int (decimal part truncated)
print(int(3.14))  # Output: 3

# 2. Converting an int to float
print(float(10))  # Output: 10.0

# 3. Converting a number to a string
print(str(25))  # Output: '25'

# 4. Converting a string to a list
print(list("abc"))  # Output: ['a', 'b', 'c']

# 5. Converting a list to a tuple
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

# 6. Converting a list to a set (removes duplicates)
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}
