"""Write a Python Program to find the factorial of a number. """

num = int(input("Enter a number:"))

fact = 1

if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print("Factorial for 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact* i
    print(f"Factorial for {num} is {fact}")