# print("hello world")

# age=int(input("Enter your age : "))

# if age<13:
#     print("child")
# elif (age>13 and age<20):
#     print("teen_age")
# elif (age>21 and age<50):
#     print("adult")
# else:
#     print("senior")

# new_age=int(input("Enter your age : "))
# day="wednesday"

# price = 12 if age >=18 else 8
# if day=="wednesday":
#     price=price-2
#     print(price)


# num=int(input("Enter your number : "))
# def square():
#     print(num**2)
#     return num**4
# square()
# new_num=square()
# print(new_num)


# num1=int(input("Enter your first number : "))
# num2=int(input("Enter your second number : "))

# def sum():
#     sum=num1+num2
#     print(sum)

# sum()

# def sum(num1,num2):
#     sum=num1+num2
#     print(sum)

# sum(num1,num2)


# def sum(num1,num2):
#     sum=num1+num2
#     print(sum)

# sum(num1,4000)


for i in range(0,21,2):
    print(i)



def recursive(num):
    if num == 0:
        return 1
    else:
        return num * recursive(num - 1)  # Recursive call with (num-1)

new_recursive = recursive(5)
print(new_recursive)  # Output: 120 (5! = 5 × 4 × 3 × 2 × 1)

class parant():
    def __init__(self,name):
        self.name=name

    def printfunction(self):
        return self.name

obj=parant("sunnyjanjua")
newobj=obj.printfunction()

print(obj.name)
print(newobj)