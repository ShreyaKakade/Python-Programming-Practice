""" Write a Python program to perform arithmetic operations (addition and division). """

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2

print(f"Addition: {num1} + {num2} = {addition}")

num3 = float(input("Enter Dividend: "))
num4 = float(input("Enter Divisor: "))

if(num4 == 0):
    print("Error: Divisor cannot be zero.")
else:
    division = num3 / num4
    print(f"Division: {num3} / {num4} = {division}")