# Sets in Python

# Introduction to Sets
"""
A set in Python is an unordered collection of unique and immutable elements. Sets are used for 
membership testing, removing duplicates, and performing mathematical set operations like union, 
intersection, and difference.
"""

# Characteristics of a Set:
"""
1. Unordered: Elements in a set do not maintain any specific order.
2. No Duplicates: A set automatically removes duplicate entries.
3. Immutable Elements: Set elements must be immutable (e.g., strings, numbers, tuples).
4. Mutable Structure: The set itself can be modified (add/remove elements).
"""

# Creating Sets
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Demonstrating no duplicates
my_set = {1, 2, 2, 3, 4, 4, 5}
print("Set without duplicates:", my_set)

# Creating an empty set
empty_set = set()
print("Empty Set:", empty_set)

# Adding Elements to a Set
my_set.add(6)
print("After Adding 6:", my_set)

# Removing Elements from a Set
my_set.remove(3)  # Raises KeyError if element not found
print("After Removing 3:", my_set)

my_set.discard(7)  # Does not raise an error if element not found
print("After Discarding 7:", my_set)

# Membership Testing
print("Is 2 in the set?", 2 in my_set)
print("Is 10 in the set?", 10 in my_set)

# Mathematical Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: Combines elements of both sets
print("Union:", set1.union(set2))

# Intersection: Common elements in both sets
print("Intersection:", set1.intersection(set2))

# Difference: Elements in one set but not the other
print("Difference (set1 - set2):", set1.difference(set2))

# Symmetric Difference: Elements in either set but not in both
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Set Methods Summary
"""
Common Set Methods:
1. add()                : Adds an element to the set.
2. remove()             : Removes an element (KeyError if not found).
3. discard()            : Removes an element (no error if not found).
4. clear()              : Removes all elements from the set.
5. copy()               : Returns a shallow copy of the set.
6. pop()                : Removes and returns an arbitrary element.
7. union()              : Returns a set containing elements from both sets.
8. intersection()       : Returns a set containing common elements.
9. difference()         : Returns a set with elements in one set but not in the other.
10. symmetric_difference(): Returns a set with elements in either but not in both sets.
11. isdisjoint()        : Returns True if two sets have no common elements.
12. issubset()          : Returns True if one set is a subset of another.
13. issuperset()        : Returns True if one set is a superset of another.
"""

# Example Program: Demonstrating Set Operations
fruits = {"apple", "banana", "cherry"}
citrus = {"orange", "lemon", "cherry"}

print("\nFruits:", fruits)
print("Citrus:", citrus)

# Union
print("Union:", fruits.union(citrus))

# Intersection
print("Intersection:", fruits.intersection(citrus))

# Difference
print("Difference (fruits - citrus):", fruits.difference(citrus))

# Symmetric Difference
print("Symmetric Difference:", fruits.symmetric_difference(citrus))

# Clear the set
fruits.clear()
print("After Clearing Fruits Set:", fruits)
