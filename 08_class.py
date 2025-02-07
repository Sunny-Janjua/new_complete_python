"""
===========================================
Lists in Python
===========================================
Definition:
A list is a mutable, ordered collection of items in Python. 
It can contain elements of different data types, including numbers, strings, 
and even other lists. Lists are one of the most commonly used data types in Python.

Key Characteristics:
1. Ordered: Elements in a list maintain their order.
2. Mutable: Lists can be modified after creation.
3. Indexed: Elements can be accessed using their index, starting from 0.

Syntax:
# Creating a list
my_list = [element1, element2, element3]
"""

# Example of a list
my_list = [10, 20, "Python", True, 3.14]
print("My List:", my_list)

"""
===========================================
Common List Methods with Examples
===========================================
"""

# 1. append() - Adds an element to the end of the list
my_list.append("New Element")
print("After append:", my_list)

# 2. insert() - Inserts an element at a specific index
my_list.insert(2, "Inserted Element")
print("After insert:", my_list)

# 3. remove() - Removes the first occurrence of a specific element
my_list.remove("Python")
print("After remove:", my_list)

# 4. pop() - Removes and returns the element at a given index (default is the last element)
popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped Element:", popped_element)

# 5. index() - Returns the index of the first occurrence of an element
index_of_true = my_list.index(True)
print("Index of True:", index_of_true)

# 6. count() - Counts the number of occurrences of an element
count_of_10 = my_list.count(10)
print("Count of 10:", count_of_10)

# 7. sort() - Sorts the list in ascending order (only works with homogeneous data types)
numbers = [5, 3, 8, 1, 4]
numbers.sort()
print("Sorted List:", numbers)

# 8. reverse() - Reverses the order of the list
numbers.reverse()
print("Reversed List:", numbers)

# 9. extend() - Adds all elements of another list to the current list
additional_numbers = [9, 7]
numbers.extend(additional_numbers)
print("After extend:", numbers)

# 10. clear() - Removes all elements from the list
numbers.clear()
print("After clear:", numbers)

"""
===========================================
Additional Functions for Lists
===========================================
"""

# len() - Returns the number of elements in a list
print("Length of my_list:", len(my_list))

# max() - Returns the maximum value in a list (works only with numeric or string lists)
numeric_list = [10, 20, 30, 40]
print("Maximum Value:", max(numeric_list))

# min() - Returns the minimum value in a list
print("Minimum Value:", min(numeric_list))

# sum() - Returns the sum of all elements in a numeric list
print("Sum of Values:", sum(numeric_list))

# List slicing - Accessing subsets of the list
print("Sliced List (0:3):", my_list[0:3])

"""
===========================================
List Comprehension
===========================================
Definition:
List comprehension is a concise way to create lists using loops and conditions.

Example: Create a list of squares for numbers from 1 to 5.
"""
squares = [x**2 for x in range(1, 6)]
print("List of Squares:", squares)

"""
===========================================
Checking Membership
===========================================
"""
print("Is 20 in my_list?", 20 in my_list)
print("Is 'Python' not in my_list?", "Python" not in my_list)

"""
===========================================
Conclusion
===========================================
Lists are powerful and versatile. Understanding their methods and how to use them
can significantly enhance your Python programming skills. 
"""
