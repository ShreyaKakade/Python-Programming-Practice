"""Write a Python Program to swap two varaibles without temp variable."""

a = input("Enter a number a:")
b = input("Enter a number b:")

print(f"Original a: {a} and b: {b}")

a, b = b, a

print(f"Swapped a: {a} and b: {b}")