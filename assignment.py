# code for simple calculator

method = input("Enter the operation (+,-,*,/):-")
input1 = int(input("Enter first number:- "))
input2 = int(input("Enter second number:- "))
if method == '+':
    print(f"The addition of {input1} and {input2} is:- {input1+input2}")
elif method == '-':
    print(f"The subtraction of {input1} and {input2} is:- {input1-input2}")
elif method == '*':
    print(f"The multiplication of {input1} and {input2} is:- {input1*input2}")
elif method == '/':
    print(f"The division of {input1} and {input2} is:- {input1/input2}")
else:
    print("None")
print("THANK YOU FOR USING THIS CALCULATOR")