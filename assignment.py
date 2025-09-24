# ------------------------------------------(Assignment - 1)---------------------------------------------


# Task (1):- Perform Basic Mathematical Operations:

'''
Problem Statement: Write a Python program that does the following:
a.  Takes two numbers as input from the user.
b.  Performs the basic mathematical operations on these two numbers:

o -  Addition
o -	Subtraction
o -	Multiplication
o -	Division

c.  Displays the results of each operation on the screen.

'''
input1 = int(input("Enter First Number: "))
input2 = int(input("Enter Second Number: "))

print(f"Addition: {input1+input2}")
print(f"Substraction: {input1-input2}")
print(f"Multiplication: {input1*input2}")
print(f"Divison: {input1/input2}")

# Task (2):- Create a Personalized Greeting:

'''
Problem Statement: Write a Python program that:
a.  Takes a user's first name and last name as input.
b.  Concatenates the first name and last name into a full name.
c.  Prints a personalized greeting message using the full name.

'''
first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")

full_name = first_name+ " " +last_name
print(f"Hello {full_name}! Welcome To The Python Program")

# ------------------------------------------(Assignment - 2)---------------------------------------------


# Task (1):- Write a Python program to take an input from the user and check if the number is even or odd:

number = int(input("Enter a number :- "))
if number % 2 == 0:
    print(number ,"is an even number")
else:
    print(number ,"is an odd number")

# Task (2):- code for adding Sum of Integers from 1 to 50 Using a Loop:

sum = 0

for number in range(0,51):
    sum = sum + number
print(f"The sum of numbers from 1 to 50 is: {sum}")

# ------------------------------------------(Assignment - 3)---------------------------------------------


# Task (1):- Calculate Factorial Using a Function:

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(4)
print(result)

# Task (2):- Using the Math Module for Calculations:

import math

try:
    number = float(input("Enter a number: "))

    if number >= 0:
        square_root = math.sqrt(number)
    else:
        square_root = "Undefined (cannot take square root of a negative number)"

    if number > 0:
        natural_log = math.log(number)
    else:
        natural_log = "Undefined (logarithm only defined for positive numbers)"

    sine_value = math.sin(number)

    print("\nResults:")
    print(f"Square root: {square_root}")
    print(f"Logarithm: {natural_log}")
    print(f"Sine : {sine_value}")

except ValueError:
    print("Invalid input. Please enter a valid number.")


# ------------------------------------------(Assignment - 5)---------------------------------------------


# Task (1):- Create a Dictonary of Student Marks:

student_dict = {
    "Alice": 56,
    "Aman": 34,
    "Archit": 54
}

student_name = input("Enter the student's name: ")

if student_name in student_dict:
    print(f"{student_name} Marks: {student_dict[student_name]}")
else:
    print(f"{student_name} Not Found")

# Task (2):- Demonstrate List Slicing:

'''
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

'''

numbers_list = [1,2,3,4,5,6,7,8,9,10]
new_list = numbers_list[:5]
print(new_list)
print(list(reversed(numbers_list[:5])))
