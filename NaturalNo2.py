"Write a Python program for cube sum of first n natural numbers"

def cube(n):
    if n <= 0:
        return 0
    else:
        total = sum([i**3 for i in range(1 , n+1)])
        return total
        
n = int(input("Enter a number:"))

if n <= 0:
    print("Invalid input")
else:
    result = cube(n)
    print(f"{result}")

