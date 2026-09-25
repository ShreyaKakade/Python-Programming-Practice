"Write a Python program to find Factorial of number using recursion"

def rec_fact(n):
    if n == 1:
        return n
    else:
        return n * rec_fact(n-1)
    
num = int(input("Enter a number:"))

if num < 0:
    print("Invalid Input")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(rec_fact(num))
    