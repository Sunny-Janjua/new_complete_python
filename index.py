# import math
# print("hello world")

# print(math.sqrt(2))
# print(math.factorial(6))
# print(math.floor(math.sqrt(2)))

# print(math.floor(math.pi))
# print(math.floor(math.sin(math.pi)))


# import math

# # Basic math operations
# print("Ceiling of 4.2:", math.ceil(4.2))
# print("Floor of 4.8:", math.floor(4.8))
# print("Factorial of 5:", math.factorial(5))
# print("Greatest Common Divisor of 8 and 12:", math.gcd(8, 12))

# # Power and logarithms
# print("e raised to the power 2:", math.exp(2))
# print("Natural log of 2.7183:", math.log(2.7183))
# print("Square root of 16:", math.sqrt(16))

# # Trigonometric functions
# print("Sine of 90 degrees (in radians):", math.sin(math.radians(90)))
# print("Cosine of 0 degrees:", math.cos(math.radians(0)))
# print("Arctangent of 1:", math.atan(1))

# # Special constants
# print("Value of Pi:", math.pi)
# print("Value of e:", math.e)



# import os
# if os.path.exists:
#     os.mkdir("sunny_test")

# for i in range(1,100):
#     os.mkdir(f"sunny_test/new_sunny_test{i+1}")




# import os
# if os.path.exists:
#     os.mkdir("sunny_test")

# for i in range(1, 100):
#     os.mkdir(f"sunny_test/new_sunny_test{i+1}")

# import os

# # Check and create parent directory
# parent_dir = "sunny_test"
# if not os.path.exists(parent_dir):
#     os.mkdir(parent_dir)

# # Create nested directories with Python files
# for i in range(1, 101):
#     nested_dir = os.path.join(parent_dir, f"new_sunny_test{i}")
#     os.makedirs(nested_dir)  # Create the nested directory
    
#     # Create a Python file in the directory
#     file_path = os.path.join(nested_dir, f"sunny{i}.py")
#     with open(file_path, "w") as file:
#         file.write(f"# This is sunny{i}.py\nprint('Hello from sunny{i}.py! 🐍✨')")

# print("Nested directories with Python files created successfully! 🚀📂📝")



# data=open("sunny.txt" , "w")
# print(data)

# print(data.read())

# data.close()

# Open the file in write mode and write content
# data = open("sunny.txt", "w")
# data.write("Hello, Sunny! Welcome to Python file handling.\n")
# data.write("This is an example of writing and reading files.\n")
# data.close()  # Always close the file after writing

# # Open the file in read mode and read content
# data = open("sunny.txt", "r")
# print(data.read())  # Read and print the content of the file
# data.close()  # Close the file after reading

class parent:
    def __init__(self,name,roll_no,email):
        self.name = name
        self.roll_no = roll_no
        self.email = email
    
new_class = parent("sunny janjua","3455","hussnainmulazam@gmail.com")
print(new_class.name)
print(new_class.roll_no)

print(new_class.email)


# Defining a class
class Person:
    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
    
    # Method to display information
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance of the class)
person1 = Person("John", 30)
person2 = Person("Alice", 25)

# Calling methods
person1.greet()  # Output: Hello, my name is John and I am 30 years old.
person2.greet()  # Output: Hello, my name is Alice and I am 25 years old.
