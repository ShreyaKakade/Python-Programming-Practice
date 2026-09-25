"""Write a Python program to check Prime Number."""

num = int(input("Enter a number:"))

if num <= 1:
    prime = False
else:
    prime = True
    
    for i in range(2,int(num ** 0.5) + 1):
        if(num % i == 0):
            prime = False
            break

if prime == False:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")