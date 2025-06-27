# Perform Basic Mathematical Operations: (Assignment -1)

# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

'''input1 = int(input("Enter First Number: "))
input2 = int(input("Enter Second Number: "))

print(f"Addition: {input1+input2}")
print(f"Substraction: {input1-input2}")
print(f"Multiplication: {input1*input2}")
print(f"Divison: {input1/input2}")
'''

# Create a Personalized Greeting: (Assignment -1)

# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

'''first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")

full_name = first_name+ " " +last_name
print(f"Hello {full_name}! Welcome To The Python Program")'''

# Write a Python program to take an input from the user and check if the number is even or odd: (Assignment -2)
"""number = int(input("Enter a number :- "))
if number % 2 == 0:
    print(number ,"is an even number")
else:
    print(number ,"is an odd number")"""

#code for adding Sum of Integers from 1 to 50 Using a Loop: (Assignment -2)

'''sum = 0

for number in range(0,51):
    sum = sum + number
print(f"The sum of numbers from 1 to 50 is: {sum}")
'''
# code for getting factorial of a  positive number: (Assignment -3)

"""def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(4)
print(result)"""

#Task 2: Using the Math Module for Calculations: (Assignment -3)

'''import math

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
    print("Invalid input. Please enter a valid number.")'''

# code for Calculate Factorial Using a Function: (Assignment -3)

'''def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")'''

#Code for fetching students marks from a Dictionary: (Assignment -5)

'''student_dict = {
    "Alice": 56,
    "Aman": 34,
    "Archit": 54
}

student_name = input("Enter the student's name: ")

if student_name in student_dict:
    print(f"{student_name} Marks: {student_dict[student_name]}")
else:
    print(f"{student_name} Not Found")'''

#Problem Statement: Write a Python program that:(Assignment -5)
'''1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''


'''numbers_list = [1,2,3,4,5,6,7,8,9,10]
new_list = numbers_list[:5]
print(new_list)
print(list(reversed(numbers_list[:5])))'''