#1. Comment : Comment are something which you wish to openly write, which you don't want it to be executed.

#This is an example of singl line comment
"""This is a multine comment"""

#2. variables : They are letter or words that act as storage which can store values

sher = "harsh bhaiya"
SheriyansSchool = "Students"      #This is known as pascalcase
sheriyansSchool = "Students"      #This is known as camelcase
sheriyans_school = "Students"     #This is known as snakecase

#3. Datatypes : Datatypes are the things we store in variable and it defines what data type variables are.

a = 12 
print(type(a))

#There are different types of Datatypes

#Integer : Integer are all the positive and negative numbers including zero , they are known as integer datatype
#example:
a = 12

#Float : The numbers with decimal value is known as float value
#example:
a1 = 2.4

#Complex : Numbers with real and imaginary parts are complex.
#example:
v = 34j

#String : This is used to store anything in python, literally anything that are available on your keyboard.
#example:
'anish' '12345'
string = 'anish'

#Boolean : Theres nothing much to say this is the data type which will and always give the result of True and False.
#example:
a = True
b = False


#String Indexing: For any word the positive indexing will begin from left to right startin with zero (0) and for negative indexing it will begin from right to left from (-1)
#Example

index = "Anish"
print(index[1]) # The output will be (n)

#String Slicing : Slicing means cutting out a slice from string and this is also done using index values
#Example 

slice = "Anish Pujari"
print(slice[0:5:1]) # Here while slicing the first value is the start index value : the next index value of where you want it to end : Th number of steps you want it take to slice
#Output will be Anish

#Type Convesion : Converting one data type to another is called type conversion using type coversion function
#Example
#int() float() str() bool() ==> These are the type conversion function

a = 12         #Here you have assigned an integer value for it , so if you check its type it will show integer type 
a = str(a)
print(type(a)) #==> “12” (a will be converted to string)

#Input and Output 

print("Hello This is a Print Statement")

name = input("Enter your name : ")
age = input("Enter your age: ")
print(f"Hello my name is  {name} and my age is {age}.")

#Task questions from the PDF
#Accept numbers from a user

Number = int(input("Enter a number please : "))
print(f"Then number enered by the user is {Number}.")

#Accept age from the user and print it.

Userage = int(input("Please type your age:"))
print(f"The user's entered age is {Userage}.")