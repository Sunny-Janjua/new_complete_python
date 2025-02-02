print("hello world")

class Parent:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def print_values(self):
        print(f"My name is {self.name}")
        print(f"My roll no is {self.roll_no}")

class Child(Parent):  # Fixed class definition
    def __init__(self, name, roll_no, age, email):
        super().__init__(name, roll_no)
        self.age = age
        self.email = email
    
    def new_print_value(self):
        print(f"My age is {self.age}")
        print(f"My email is {self.email}")

# Creating an object of Child class
obj = Child("Sunny Janjua", 3455, 45, "hussnainmulazam@gmail.com")
obj.print_values()
obj.new_print_value()  # Fixed missing parentheses



class Parent:
    def __init__(self, name, rollNo, age):
        self.__name = name
        self.rollNo = rollNo
        self.age = age

    def input_values(self):
        self.__name = input("Enter your name: ")  # Now storing user input in instance variables
        self.rollNo = input("Enter your roll no: ")
        self.age = int(input("Enter your age: "))

    def print_values(self):
        print(f"My name is {self.__name}")
        print(f"My roll no is {self.rollNo}")
        print(f"My age is {self.age}")

class Child(Parent):
    def __init__(self, name, rollNo, age, email):
        super().__init__(name, rollNo, age)
        self.email = email

    def new_print_values(self):
        print(f"My email is {self.email}")

# Correct object creation with all required arguments
obj = Child("Sunny Janjua", "3455", 25, "hussnainmulazam@gmail.com")

# Now, we take input and print details
obj.input_values()  # User will enter their own data
obj.print_values()
obj.new_print_values()
