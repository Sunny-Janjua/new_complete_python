# print("Hello World!")
# num1 =float(input("Please enter your number : "))
# num2 =float(input("Please enter your number : "))

# sum = num1 + num2
# print(f"the sum of the two numbers is : {sum}")

# product = num1 * num2
# print(f"the product of the two numbers is : {product}")

# difference = num1 - num2
# print(f"the difference of the two numbers is : {difference}")

# division = num1 / num2
# print(f"the division of the two numbers is : {division}")

# modulus = num1 % num2
# print(f"the modulus of the two numbers is : {modulus}")

# power = num1 ** num2
# print(f"the power of the two numbers is : {power}")

# floor_division = num1 // num2
# print(f"the floor division of the two numbers is : {floor_division}")


# base=int(input("Enter the base of the triangle : "))
# height=int(input("Enter the height of the triangle : "))
# area = 0.5 * base * height
# print(f"The area of the triangle is : {area}")

# radius=int(input("Enter the radius of the circle : "))
# area = 3.142 * radius * radius
# print(f"The area of the circle is : {area}")

# side1=int(input("Enter the length of the first side of the triangle : "))
# side2=int(input("Enter the length of the second side of the triangle : "))

# if side1 + side2 <= 0:
#     print("Invalid input")
# else:
#     print("valid input")


# new_number1 = int(input("Enter the first number : "))
# new_number2 = int(input("Enter the second number : "))
# swap = new_number1

# new_number1 = new_number2

# new_number2 = swap

# print(f"After swapping the values, the first number is : {new_number1}")

# print(f"After swapping the values, the second number is : {new_number2}")

# number = int(input("Enter a number : "))

# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# age = int(input("Enter your age : "))

# if age < 18:
#     print("You are a minor")
# else:
#     print("You are an adult")

# import  random
# number = random.randint(1, 100)
# print(number)
# import random
# new_number = random.randint(1, 100)

# print(f"The new number is : {new_number}")

# kilometres = float(input("Enter the distance in kilometres : "))
# meter=0.621371
# miles =  meter* kilometres
# print(f"The distance in miles is : {miles}")

# celsius = float(input("Enter the temperature in Celsius : "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"The temperature in Fahrenheit is : {fahrenheit}")

# fahrenheit = float(input("Enter the temperature in Fahrenheit : "))
# celsius = (fahrenheit - 32) * 5/9
# print(f"The temperature in Celsius is : {celsius}")



# import calendar

# year = int(input("Enter the year : "))
# month = int(input("Enter the month : "))
# cal=calendar.month(year, month)
# print(f"The calendar for the month is : {cal}")

# year = 2023
# print(calendar.calendar(year))

# # Print the calendar for a specific month of a specific year
# year = 2023
# month = 10
# print(calendar.month(year, month))

# # Check if a year is a leap year
# year = 2024
# is_leap = calendar.isleap(year)
# print(f"Is {year} a leap year? {is_leap}")

# # Get the number of leap years in a range of years
# start_year = 2000
# end_year = 2023
# leap_days = calendar.leapdays(start_year, end_year)
# print(f"Number of leap years between {start_year} and {end_year}: {leap_days}")

# # Get the weekday of the first day of the month and the number of days in the month
# year = 2023
# month = 10
# first_weekday, num_days = calendar.monthrange(year, month)
# print(f"First weekday: {first_weekday}, Number of days: {num_days}")

# year = 2023
# month = 10
# day = 15
# day_of_week = calendar.weekday(year, month, day)
# print(f"Day of the week for {year}-{month}-{day}: {day_of_week}")

# year = 2023
# month = 10
# month_matrix = calendar.monthcalendar(year, month)
# print(f"Month matrix for {year}-{month}:")
# for week in month_matrix:
#     print(week)

# print("Days of the week:")
# for day in calendar.day_name:
#     print(day)

# print("Months of the year:")
# for month in calendar.month_name:
#     print(month)


# import  math


# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: ")) 

# discriminant = b**2 - 4*a*c 

# if discriminant > 0:  
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)   
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)    
#     print(f"Root 1: {root1}")    
#     print(f"Root 2: {root2}")
# elif discriminant == 0: 
#     root = -b / (2*a)    
#     print(f"Root: {root}")
# else:   
#     real_part = -b / (2*a)    
#     imaginary_part = math.sqrt(abs(discriminant)) / (2*a)    
#     print(f"Root 1: {real_part} + {imaginary_part}i")    
#     print(f"Root 2: {real_part} - {imaginary_part}i") 


# print("1")
# print("2")
# print("3")
# print("4")
# print("5")

# num1 = 104
# num2 = 1043
# num3 = 102
# num4 = 106
# num5 = 1098
# print(f"my number is {num1}")
# print(f"my number is {num2}")
# print(f"my number is {num3}")
# print(f"my number is {num4}")
# print(f"my number is {num5}")



# array.append("sunny janjua")
# print(array)

# print(array[0])
# print(array[1])
# print(array[3])
# print(array[4])
# print(array[9])

# array:list = [104, 1043, 102,102, 106, 1098 ,"hussnian","awais","danish","ali","usman",3434.3223,True,False]
# print(f"my list is {array}")

# print(array.index(102))
# print(array.pop(4))
# print(array)

# array.insert(4,"hello world")
# print(array)

# print(array.count(102))

# array.extend([1,2,3,4,5,6,7,8,9])

# print(array)

# newlist:list = [1,2,36878,88,45,3234,4,5,6,7,8,9]
# sum=array+newlist

# print(f"my new list is {sum}")
# newlist.remove(9)
# print(newlist)

# newlist.sort()

# print(newlist)
# newlist.clear()

# print(newlist)


# year=int(input("Please enter year : "))
# if (year%4==0 and year%100==0 and year%400==0):
#     print("The year is a leap year")
# else:
#     # comment: 
#     print("The year is not a leap year")

# if (year % 400 == 0) and (year % 100 == 0):  
#       print("{0} is a leap year".format(year)) 
# elif (year % 4 ==0) and (year % 100 != 0):  
#       print("{0} is a leap year".format(year)) 
# else:   
#      print("{0} is not a leap year".format(year))



# year=int(input("Please enter year : "))
# if (year%4==0 and year%100==0 and year%400==0):
#     print(f"Leap year : {year}")
# else:
#     print(f"Not leap year : {year}")


# string:str="code with sunny janjua"
# print(f"our string is = {string}")

# new_str=string.upper()
# print(f"my is string is = {new_str}")

# new_str=string.lower()
# print(f"my is string is = {new_str}")

# new_str=string.replace("sunny","hussnain mulazam")
# print(f"my is string is = {new_str}")

# new_str=string.count("hussnain")
# print(f"my is string is = {new_str}")

# print(f"my is string is = {new_str}")
# print(string.count("hussnain"))


# new_str=string.title()
# print(f"my is string is = {new_str}")


# new_str=string.capitalize()
# print(f"my is string is = {new_str}")

# text = "Hello World"
# print(text.swapcase())  # Output: "hELLO wORLD"


# string.swapcase()
# print(f"my is string is = {string}")


# new_string="hello world"

# print(new_string.swapcase())


# text = "hello world"
# print(text.index("o"))  # Output: 4


# new_string="sunny janjua"
# print(new_string.index("n"))

# print(new_string.count("n"))

# end while

# i=1
# table=int(input("Please enter your table number : "))
# while (i<=10):
#     print(f"my number is {table} * {i} = {table*i}")
#     i+=1


# sum=0
# i=1
# while (i<=5):
#     sum=sum+i
#     print(sum)
#     i+=1


# num = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, num + 1):
#     factorial *= i

# print(f"Factorial of {num} is {factorial}")

# num1 = int(input("Please enter number : "))
# factorial=1

# for i in range(1,num1+1):
#     factorial=factorial*i
# print(f"Our factorial is {factorial}")


# num = int(input("Enter a number: ")) 
# flag = False
 
# if num == 1:    
#     print(f"{num}, is not a prime number")
# elif num > 1:  
#     for i in range(2, num):        
#         if (num % i) == 0:            
#             flag = True   
#             break
# if flag:   
#      print(f"{num}, is not a prime number")
# else:   
#      print(f"{num}, is a prime number")


# startNumber = int(input("Please enter start number : "))
# endNumber = int(input("Please enter  end number : "))


# for i in (startNumber, endNumber + 1):
#     if (i>1):
#         for j in (2,i+1):
#             if (j%i==0):
#                 break
#         else:
#             print(j)

# lower = 1
# upper = 10
# print("Prime numbers between", lower, "and", upper, "are:") 
# for num in range(lower, upper + 1): 
#    if num > 1:        
#     for i in range(2, num):            
#         if (num % i) == 0:                
#             break
#     else:            
#         print(num)

# num = int(input("Enter a number: "))
# factorial = 1
# if num <0:    
#     print("Factirial does not exist for negative numbers")
# elif num == 0:    
#     print("Factorial of 0 is 1")
# else:    
#     for i in range(1, num+1):        
#         factorial = factorial*i    
#     print(f'The factorial of {num} is {factorial}')

# num = int(input("Display multiplication table of: ")) 
# for i in range(1, 11):    
#     print(f"{num} X {i} = {num*i}")

# naturalNumber = int(input("Please enter natural number : "))
# sum=0
# for i in range(naturalNumber+1):
#     sum=sum+i
# print(f"sum is {sum}")

# limit = int(input("Enter the limit: ")) 
# sum = 0 
# for i in range(1, limit + 1):    
#     sum += i 
# print("The sum of natural numbers up to", limit, "is:", sum)


# char = str(input("Enter the character: "))
# print("The ASCII value of '" + char + "' is", ord(char))


# age = int(input("Enter your age: "))
# day = "wednesday"

# if age >= 18:
#     price = 12
# else:
#     price = 8

# if day == "wednesday":
#     price -= 2

# print(price)

# number=lambda x: x**4
# print("my number is : ",number(4))


def sumall(*args):
    return sum(args)

print(sumall(44,44,4))

def calculate_all(*args):
    total_sum = sum(args)
    total_product = 1
    for num in args:
        total_product *= num

    if len(args) > 1:
        total_division = args[0]
        for num in args[1:]:
            total_division /= num
    else:
        total_division = args[0]  # If only one number is provided, return it as is.

    return total_sum, total_product, total_division

# Example usage
sum_result, product_result, division_result = calculate_all(44, 44, 4)
print(f"Sum: {sum_result}, Product: {product_result}, Division: {division_result}")



class Person:
    pass  # An empty block
p = Person()
print(p)

class Bird:

    def __init__(self):
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')

    def swim(self):
        print('Swim faster')

# child class
class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print('Penguin is ready')

    def whoisThis(self):
        print('Penguin')

    def run(self):
        print('Run faster')

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()