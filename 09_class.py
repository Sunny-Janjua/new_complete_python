"""
===========================================
Tuples in Python
===========================================

Definition:
A tuple is an **immutable**, **ordered** collection of elements. 
Like lists, tuples can contain elements of different data types.
However, once a tuple is created, its elements cannot be changed, added, or removed.

Key Characteristics:
1. **Immutable**: Tuples cannot be modified after creation.
2. **Ordered**: The order of elements is preserved.
3. **Heterogeneous**: Can store elements of different types.
4. **Indexed**: Elements can be accessed using their index.

Syntax:
# Creating a tuple
my_tuple = (element1, element2, element3)

Tuples can also be created without parentheses (using a comma-separated sequence of elements):
my_tuple = element1, element2, element3
"""

# Example of a tuple
my_tuple = (10, 20, "Python", True, 3.14)
print("My Tuple:", my_tuple)

"""
===========================================
Tuple Methods with Examples
===========================================
"""

# 1. count() - Counts the number of occurrences of a specific element in the tuple
count_of_20 = my_tuple.count(20)
print("Count of 20 in my_tuple:", count_of_20)

# 2. index() - Returns the index of the first occurrence of a specific element
index_of_python = my_tuple.index("Python")
print("Index of 'Python' in my_tuple:", index_of_python)

"""
===========================================
Operations on Tuples
===========================================
"""

# 1. Accessing Elements
print("First Element:", my_tuple[0])  # Accessing the first element
print("Last Element:", my_tuple[-1])  # Accessing the last element

# 2. Slicing Tuples
print("Sliced Tuple (1:4):", my_tuple[1:4])  # Get elements from index 1 to 3

# 3. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# 4. Repetition
repeated_tuple = tuple1 * 2
print("Repeated Tuple:", repeated_tuple)

"""
===========================================
Additional Functions for Tuples
===========================================
"""

# 1. len() - Returns the number of elements in the tuple
print("Length of my_tuple:", len(my_tuple))

# 2. max() - Returns the maximum value in the tuple (only works with comparable elements)
numeric_tuple = (5, 3, 8, 1, 4)
print("Maximum Value:", max(numeric_tuple))

# 3. min() - Returns the minimum value in the tuple
print("Minimum Value:", min(numeric_tuple))

# 4. sum() - Returns the sum of elements in a numeric tuple
print("Sum of Values:", sum(numeric_tuple))

"""
===========================================
Tuple Unpacking
===========================================
Definition:
Tuple unpacking allows you to assign elements of a tuple to multiple variables at once.
"""
coordinates = (10, 20, 30)
x, y, z = coordinates
print("Unpacked Coordinates:", x, y, z)

"""
===========================================
Nested Tuples
===========================================
Definition:
Tuples can contain other tuples as elements, enabling the creation of complex structures.
"""
nested_tuple = (1, (2, 3), (4, (5, 6)))
print("Nested Tuple:", nested_tuple)
print("Accessing Nested Element:", nested_tuple[2][1][1])  # Accessing 6

"""
===========================================
Membership Testing
===========================================
"""
print("Is 20 in my_tuple?", 20 in my_tuple)
print("Is 'Java' not in my_tuple?", "Java" not in my_tuple)

"""
===========================================
Immutable Nature of Tuples
===========================================
# Trying to modify a tuple will result in a TypeError
# Uncomment the lines below to see the error:

# my_tuple[1] = 25  # Error: Tuples are immutable
# del my_tuple[1]   # Error: Cannot delete individual elements in a tuple
"""

"""
===========================================
When to Use Tuples?
===========================================
1. When the data should remain constant.
2. When you want to use a sequence as a key in a dictionary (since tuples are hashable).
3. When you want to store fixed collections of related data, such as coordinates.

"""

"""
===========================================
Conclusion
===========================================
Tuples are a versatile and efficient data type in Python.
They are ideal for storing immutable sequences of data and have simple, intuitive methods.
"""

