"""
===========================================
Dictionaries in Python
===========================================

Definition:
A dictionary in Python is an unordered, mutable, and indexed collection 
of key-value pairs. Each key must be unique and immutable, while values 
can be of any data type and may repeat.

Key Characteristics:
1. Unordered: Items do not have a fixed position.
2. Mutable: Can add, update, or remove key-value pairs.
3. Indexed by Keys: Access values using their corresponding keys.
4. Keys are unique and immutable (e.g., strings, numbers, or tuples).

Syntax:
# Creating a dictionary
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
"""

# Example of a dictionary
my_dict = {
    "name": "Hussnain",
    "age": 22,
    "city": "Lahore",
    "is_student": True
}
print("My Dictionary:", my_dict)

"""
===========================================
Accessing Elements in a Dictionary
===========================================
"""

# Accessing values using keys
print("Name:", my_dict["name"])

# Using the get() method to access a value
print("Age:", my_dict.get("age"))

# Accessing a non-existing key with get() (returns None instead of an error)
print("Country:", my_dict.get("country"))

"""
===========================================
Adding and Updating Dictionary Items
===========================================
"""

# Adding a new key-value pair
my_dict["country"] = "Pakistan"
print("After Adding Country:", my_dict)

# Updating an existing key
my_dict["age"] = 23
print("After Updating Age:", my_dict)

"""
===========================================
Removing Items from a Dictionary
===========================================
"""

# Removing an item using pop()
removed_item = my_dict.pop("city")
print("After Popping 'city':", my_dict)
print("Removed Item:", removed_item)

# Removing the last inserted item using popitem()
last_item = my_dict.popitem()
print("After Popitem:", my_dict)
print("Last Item Removed:", last_item)

# Deleting a key-value pair using del
del my_dict["is_student"]
print("After Deleting 'is_student':", my_dict)

# Clearing all items from the dictionary
my_dict.clear()
print("After Clearing:", my_dict)

"""
===========================================
Dictionary Methods with Examples
===========================================
"""

# Reinitializing the dictionary
my_dict = {
    "name": "Hussnain",
    "age": 22,
    "city": "Lahore",
    "is_student": True
}

# 1. keys() - Returns a view object of keys
print("Keys:", my_dict.keys())

# 2. values() - Returns a view object of values
print("Values:", my_dict.values())

# 3. items() - Returns a view object of key-value pairs
print("Items:", my_dict.items())

# 4. update() - Updates the dictionary with another dictionary or key-value pairs
additional_info = {"country": "Pakistan", "hobby": "Coding"}
my_dict.update(additional_info)
print("After Update:", my_dict)

"""
===========================================
Looping Through Dictionaries
===========================================
"""

# Looping through keys
for key in my_dict.keys():
    print("Key:", key)

# Looping through values
for value in my_dict.values():
    print("Value:", value)

# Looping through key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

"""
===========================================
Nested Dictionaries
===========================================
"""

# Creating a nested dictionary
nested_dict = {
    "person1": {"name": "Hussnain", "age": 22},
    "person2": {"name": "Amna", "age": 21}
}
print("Nested Dictionary:", nested_dict)

# Accessing nested dictionary elements
print("Person1 Name:", nested_dict["person1"]["name"])

"""
===========================================
Common Dictionary Functions
===========================================
"""

# len() - Returns the number of items in the dictionary
print("Number of Items:", len(my_dict))

# in - Checks if a key exists in the dictionary
print("Is 'name' a key in my_dict?", "name" in my_dict)

"""
===========================================
When to Use Dictionaries?
===========================================
1. When data needs to be organized as key-value pairs.
2. When fast lookups are required using unique keys.
3. For representing real-world data structures like JSON objects.

"""
