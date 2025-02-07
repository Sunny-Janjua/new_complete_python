# class parent:
#     def __init__(self,name,email,password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def all_information(self):
#         return f"Name: {self.name}, Email: {self.email}, Password: {self.password}"
    
#     def change_password(self, new_password):
#         return f"My password: {self.new_password}"
    
# class child(parent):
#     def __init__(self, name, email, password, age, gender):
#         super().__init__(name, email, password)
#         self.age = age
#         self.gender = gender

#     def new_all_information(self):
#         return f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Age: {self.age}, Gender: {self.gender}"
    
#     def update_age(self, new_age):
#         return f"My new age: {self.new_age}"

# # Create objects


# child_obj = child("Jane Doe", "janedoe@example.com", "secret123", 25, "Female")

# print(child_obj.all_information())
# print(child_obj.new_all_information())



# class Parent:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def all_information(self):
#         return f"Name: {self.name}, Email: {self.email}, Password: {self.password}"
    
#     def change_password(self, new_password):
#         self.password = new_password
#         return f"My password is now: {self.password}"
    
# class Child(Parent):
#     def __init__(self, name, email, password, age, gender):
#         super().__init__(name, email, password)
#         self.age = age
#         self.gender = gender

#     def new_all_information(self):
#         return f"Name: {self.name}, Email: {self.email}, Password: {self.password}, Age: {self.age}, Gender: {self.gender}"
    
#     def update_age(self, new_age):
#         self.age = new_age
#         return f"My new age is: {self.age}"

# # Creating an object for you (Hussnain Mulazam)
# child_obj = Child("Hussnain Mulazam", "hussnainmulazam@gmail.com", "your_password_here", 22, "Male")

# # Printing the information
# print(child_obj.all_information())          # Parent class method
# print(child_obj.new_all_information())      # Child class method

# # Example: Changing the password and updating age
# child_obj.change_password("new_secure_password")
# child_obj.update_age(23)

# # Print updated information
# print(child_obj.new_all_information())      # After updates




# class newParent():
#     def  __init__(self,name,roll_no,email):
#         self.name = name
#         self.roll_no = roll_no
#         self.email = email


#     def all_information(self):
#         return f"Name: {self.name}, Roll No: {self.roll_no}, Email: {self.email}"
    
# new_class = newParent("sunny janjua","3455","hussnainmulazam@gmail.com")
# print(new_class.name)
# print(new_class.roll_no)
# print(new_class.email)
# print(new_class.all_information())
        

class Parent:
    def __init__(self, name, roll_no, email, all_information, occupation, role, gender):
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.all_information = all_information
        self.occupation = occupation
        self.role = role
        self.gender = gender
    
    def get_all_information(self):
        # Taking user input and updating the attributes
        self.name = input("Enter the name: ")
        self.roll_no = input("Enter the roll number: ")
        self.email = input("Enter the email: ")
        self.all_information = input("Enter additional information: ")
        self.occupation = input("Enter the occupation: ")
        self.role = input("Enter the role: ")
        self.gender = input("Enter the gender: ")
    
    def display_information(self):
        # Displaying all stored information
        return f"Name: {self.name}, Roll No: {self.roll_no}, Email: {self.email}, " \
               f"Additional Information: {self.all_information}, Occupation: {self.occupation}, " \
               f"Role: {self.role}, Gender: {self.gender}"


class Child1(Parent):
    def __init__(self, name, roll_no, email, all_information, occupation, role, gender, child_name, child_roll_no, child_email, child_occupation):
        super().__init__(name, roll_no, email, all_information, occupation, role, gender)
        self.child_name = child_name
        self.child_roll_no = child_roll_no
        self.child_email = child_email
        self.child_occupation = child_occupation

    def get_all_information_child1(self):
        # Taking user input and updating the attributes of child1
        self.child_name = input("Enter the child's name: ")
        self.child_roll_no = input("Enter the child's roll number: ")
        self.child_email = input("Enter the child's email: ")
        self.child_occupation = input("Enter the child's occupation: ")

    def display_information_child1(self):
        # Displaying all stored information of child1
        return f"Child's Name: {self.child_name}, Child's Roll No: {self.child_roll_no}, Child's Email: {self.child_email}, " \
               f"Child's Occupation: {self.child_occupation}"


class Child2(Child1):
    def __init__(self, name, roll_no, email, all_information, occupation, role, gender, child_name, child_roll_no, child_email, child_occupation, child2_name, child2_roll_no, child2_email, child2_occupation):
        super().__init__(name, roll_no, email, all_information, occupation, role, gender, child_name, child_roll_no, child_email, child_occupation)
        self.child2_name = child2_name
        self.child2_roll_no = child2_roll_no
        self.child2_email = child2_email
        self.child2_occupation = child2_occupation

    def get_all_information_child2(self):
        # Taking user input and updating the attributes of child2
        self.child2_name = input("Enter the second child's name: ")
        self.child2_roll_no = input("Enter the second child's roll number: ")
        self.child2_email = input("Enter the second child's email: ")
        self.child2_occupation = input("Enter the second child's occupation: ")

    def display_information_child2(self):
        # Displaying all stored information of child2
        return f"Second Child's Name: {self.child2_name}, Second Child's Roll No: {self.child2_roll_no}, Second Child's Email: {self.child2_email}, " \
               f"Second Child's Occupation: {self.child2_occupation}"


# Creating an object and collecting/displaying information
obj = Child2(
    name="Parent Name", roll_no="1", email="parent@example.com", all_information="N/A", occupation="Engineer", role="Father", gender="Male",
    child_name="Child1 Name", child_roll_no="101", child_email="child1@example.com", child_occupation="Student",
    child2_name="Child2 Name", child2_roll_no="102", child2_email="child2@example.com", child2_occupation="Student"
)

# Collect information
obj.get_all_information()
print(obj.display_information())

obj.get_all_information_child1()
print(obj.display_information_child1())

obj.get_all_information_child2()
print(obj.display_information_child2())



