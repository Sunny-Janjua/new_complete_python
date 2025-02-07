"""
Python String Methods - Complete Guide with Examples
-----------------------------------------------------
This script demonstrates all important Python string methods with detailed explanations.
Run this file to see the output of each method in action!
"""

# Case Conversion Methods
text = "hello world"
print("1. upper():", text.upper())  # Converts to uppercase
print("2. lower():", text.lower())  # Converts to lowercase
print("3. title():", text.title())  # Capitalizes each word
print("4. capitalize():", text.capitalize())  # Capitalizes the first letter
print("5. swapcase():", text.swapcase())  # Swaps case

# Checking & Validation Methods
text = "Hello123"
print("6. isalpha():", text.isalpha())  # False (contains numbers)
text = "12345"
print("7. isdigit():", text.isdigit())  # True (only digits)
text = "Hello123"
print("8. isalnum():", text.isalnum())  # True (letters & numbers)
text = "   "
print("9. isspace():", text.isspace())  # True (only spaces)
text = "Hello World"
print("10. istitle():", text.istitle())  # True (Title Case)
text = "hello"
print("11. islower():", text.islower())  # True (all lowercase)
text = "HELLO"
print("12. isupper():", text.isupper())  # True (all uppercase)

# Searching & Finding Methods
text = "hello world"
print("13. find('o'):", text.find("o"))  # Finds first occurrence
print("14. count('l'):", text.count("l"))  # Counts occurrences
print("15. startswith('hello'):", text.startswith("hello"))  # True
print("16. endswith('world'):", text.endswith("world"))  # True

# Modifying & Replacing Methods
text = "hello world"
print("17. replace('world', 'Python'):", text.replace("world", "Python"))
text = "  hello  "
print("18. strip():", text.strip())  # Removes spaces
print("19. lstrip():", text.lstrip())  # Removes left spaces
print("20. rstrip():", text.rstrip())  # Removes right spaces

# Splitting & Joining Methods
text = "apple,banana,grape"
print("21. split(','):", text.split(","))  # Splits into a list
words = ["Hello", "World"]
print("22. join('-'):", "-".join(words))  # Joins list into a string

# String Formatting Methods
name = "Sunny"
age = 25
print("23. format() example:", "Hello, my name is {} and I am {} years old.".format(name, age))
print(f"24. f-string example: Hello, my name is {name} and I am {age} years old.")

# Padding & Alignment Methods
text = "42"
print("25. zfill(5):", text.zfill(5))  # Pads with zeros
text = "hello"
print("26. center(10):", text.center(10))  # Centers text
print("27. ljust(10):", text.ljust(10))  # Left-aligns text
print("28. rjust(10):", text.rjust(10))  # Right-aligns text

print("\n✅ All string methods demonstrated successfully!")
