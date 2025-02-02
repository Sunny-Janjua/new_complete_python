# 🖊️ Python - Complete Guide

## 📌 Introduction
Python is a high-level, interpreted programming language known for its **simplicity, readability, and versatility**. It supports multiple programming paradigms, including **procedural, object-oriented, and functional programming**.

Developed by **Guido van Rossum**, Python is widely used in **web development, data science, machine learning, automation, scripting, and more**.

---

## 🎯 Features of Python
- **Simple & Readable** - Easy-to-learn syntax.
- **Interpreted Language** - No need for compilation.
- **Cross-Platform** - Works on Windows, Linux, macOS.
- **Dynamically Typed** - No need to declare variable types.
- **Huge Libraries** - Extensive support for libraries like NumPy, Pandas, Django, Flask, TensorFlow.
- **Object-Oriented** - Supports OOP concepts like classes and inheritance.

---

## 🛠 Installation Guide
### 🔹 Install Python (Windows, Mac, Linux)
1. Download Python from the official site: [Python.org](https://www.python.org/)
2. Install and **check version**:  
   ```sh
   python --version
   ```
3. Run Python in the terminal:  
   ```sh
   python
   ```

---

## 🚀 Python Basics
### 🔹 1. Hello World! 🌍
```python
print("Hello, World!")
```

### 🔹 2. Variables & Data Types
```python
name = "Sunny Janjua"  # String
age = 25  # Integer
height = 5.9  # Float
is_dev = True  # Boolean

print(f"My name is {name}, I am {age} years old.")
```

### 🔹 3. Conditional Statements
```python
x = 10
if x > 5:
    print("X is greater than 5")
elif x == 5:
    print("X is 5")
else:
    print("X is less than 5")
```

### 🔹 4. Loops (For & While)
```python
# For Loop
for i in range(1, 6):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### 🔹 5. Functions in Python
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Sunny"))
```

---

## 🏗️ Object-Oriented Programming (OOP)
### 🔹 6. Classes & Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

p1 = Person("Sunny", 25)
p1.introduce()
```

### 🔹 7. Inheritance in Python
```python
class Parent:
    def display(self):
        print("I am a Parent class")

class Child(Parent):
    def show(self):
        print("I am a Child class")

obj = Child()
obj.display()
obj.show()
```

---

## 🛋️ Python Modules & Packages
### 🔹 8. Importing Modules
```python
import math
print(math.sqrt(16))
```

### 🔹 9. Creating a Custom Module
**my_module.py**
```python
def greet(name):
    return f"Hello, {name}!"
```
**main.py**
```python
import my_module

print(my_module.greet("Sunny"))
```

---

## 🗃️ File Handling
### 🔹 10. Reading & Writing Files
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 🔥 Python Advanced Topics
### 🔹 11. Exception Handling
```python
try:
    x = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution Completed.")
```

### 🔹 12. List Comprehensions
```python
numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)  # Output: [0, 2, 4, 6, 8]
```

---

## 📊 Python for Data Science
### 🔹 13. NumPy (Numerical Python)
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Output: [2 4 6 8]
```

### 🔹 14. Pandas (Data Analysis)
```python
import pandas as pd

data = {'Name': ['Sunny', 'Ali'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)
```

---

## 🌐 Python for Web Development
### 🔹 15. Flask (Web Framework)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🔥 Conclusion
Python is a **powerful and easy-to-learn language** with applications in **web development, data science, AI, machine learning, automation, and more**. 🚀  

Start **coding in Python today** and build amazing projects! 🎯  

---

## 📚 Resources
- **Official Python Docs**: [Python.org](https://www.python.org/)
- **Learn Python**: [W3Schools](https://www.w3schools.com/python/)
- **Python for AI/ML**: [TensorFlow](https://www.tensorflow.org/)

