""" Write a Python program to swap two variables. """

num1 = float(input("Enter a first number:"))
num2 = float(input("Enter a second number:"))

print(f"Original num1: {num1} and num2: {num2}")
temp = num1;
num1 = num2;
num2 = temp;

print(f"Swapped num1: {num1} and num2: {num2}")