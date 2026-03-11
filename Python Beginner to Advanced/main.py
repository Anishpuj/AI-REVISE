# #1. Comment : Comment are something which you wish to openly write, which you don't want it to be executed.

# Single line comment
# """This is a multine comment"""

# #2. variables : They are letter or words that act as storage which can store values

# sher = "harsh bhaiya"
# SheriyansSchool = "Students"  # This is known as pascalcase
# sheriyansSchool = "Students"  # This is known as camelcase
# sheriyans_school = "Students" # This is known as snakecase

# #3. Datatypes : Datatypes are the things we store in variable and it defines what data type variables are.

# a = 12 
# print(type(a))

# # There are different types of Datatypes

# # Integer : Integer are all the positive and negative numbers including zero , they are known as integer datatype
# # example:
# a = 12

# # Float : The numbers with decimal value is known as float value
# # example:
# a1 = 2.4

# # Complex : Numbers with real and imaginary parts are complex.
# # example:
# v = 34j

# # String : This is used to store anything in python, literally anything that are available on your keyboard.
# # example:
# 'anish' '12345'
# string = 'anish'

# # Boolean : Theres nothing much to say this is the data type which will and always give the result of True and False.
# # example:
# a = True
# b = False


# String Indexing: For any word the positive indexing will begin from left to right startin with zero (0) and for negative indexing it will begin from right to left from (-1)
# Example

# index = "Anish"
# print(index[1]) # The output will be (n)

# String Slicing : Slicing means cutting out a slice from string and this is also done using index values
# Example 

# slice = "Anish Pujari"
# print(slice[0:5:1]) # Here while slicing the first value is the start index value : the next index value of where you want it to end : Th number of steps you want it take to slice
# # Output will be Anish

# Type Convesion : Converting one data type to another is called type conversion using type coversion function
# Example
# int() float() str() bool() ==> These are the type conversion function

# a = 12         # Here you have assigned an integer value for it , so if you check its type it will show integer type 
# a = str(a)
# print(type(a)) # ==> “12” (a will be converted to string)

# Input and Output 

# print("Hello This is a Print Statement")

# name = input("Enter your name : ")
# age = input("Enter your age: ")
# print(f"Hello my name is  {name} and my age is {age}.")

# #Task questions from the PDF
# #Accept numbers from a user

# Number = int(input("Enter a number please : "))
# print(f"Then number enered by the user is {Number}.")

# #Accept age from the user and print it.

# Userage = int(input("Please type your age:"))
# print(f"The user's entered age is {Userage}.")


# operators : Operators are the symbols which perform operations on variables and values.
# Example : + - * / % // **
# a = 12
# b = 5
# print(a+b) #Addition
# print(a-b) #Subtraction
# print(a*b) #Multiplication
# print(a/b) #Division
# print(a%b) #Modulus
# print(a//b) #Floor Division
# print(a**b) #Exponentiation  

# print(126 > 130)
# print((456 == 456) != (235 == 236))
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# print(True and bool(0))

# Truth Tables for Logical Operators

# print("\n=== AND Operator Truth Table ===")
# print(f"True and True = {True and True}")
# print(f"True and False = {True and False}")
# print(f"False and True = {False and True}")
# print(f"False and False = {False and False}")

# print("\n=== OR Operator Truth Table ===")
# print(f"True or True = {True or True}")
# print(f"True or False = {True or False}")
# print(f"False or True = {False or True}")
# print(f"False or False = {False or False}")

# print("\n=== NOT Operator Truth Table ===")
# print(f"not True = {not True}")
# print(f"not False = {not False}")


# If Statement
# Example
condition = True
if condition:
     print("Statements to be executed if condition is true")

# age = int(input("How old are you? "))
age = 25
if age >= 18:
     print("You are an adult")

# If Else Statement
# Example
condition = False
if condition:
     print("Statements to be executed if condition is true")
else:
     print("Statements to be executed if condition is false")

# age = int(input("How old are you? "))
age = 16
if age >= 18:
     print("You are an adult")
else:
     print("You are not an adult")

# If-elif-else Statement
# Example
condition1 = False
condition2 = True
condition3 = False
if condition1:
     print("Statements to be executed if condition1 is true")
elif condition2:
     print("Statements to be executed if condition1 is false and condition2 is true")
elif condition3:
     print("Statements to be executed if condition1 and condition2 are false")
else:
     print("Statements to be executed if none of the conditions are true")

age = int(input("How old are you? "))
if age >= 65:
     print("You are eligible for senior citizen discount")
elif age >= 18 and age < 65:
     print("You are eligible for general admission")
elif age >= 3 and age < 18:
     print("You are eligible for child admission")
else:
     print("You are not eligible for any admission")


#Q1. Accept two numbers and print the greatest between them.
     num1 = int(input("Enter the first number: "))
     num2 = int(input("Enter the second number: "))
     if num1 > num2:
          print("The greatest number is: ", num1)
     else:
          print("The greatest number is: ", num2)

#Q2. Accept the gender from the user as char and print the
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)
gender = input("Enter your gender (M/F): ")
if gender == 'M':
     print("Good Morning Sir")
elif gender == 'F':
     print("Good Morning Ma'am")
else:
     print("Invalid gender")

#Accept an integer and check whether it is an even number or odd.
number = int(input("Enter an integer: "))
if number % 2 == 0:
     print("The number is even")
else:
     print("The number is odd")


#Accept name and age from the user. Check if the user is a valid voter or not. Ex- “hello shery you are a valid voter”
name = char(input("Enter your name: "))
age = int(input("Enter your age: "))
if age >= 18:
     print("Hello", name, "you are a valid voter")
else:
     print("Hello", name, "you are not a valid voter")

#Accept a year and check if it a leap year or not
year = int(input("Enter a year: "))
if year % 4 == 0:
     print("The year is a leap year")
else:
     print("The year is not a leap year")