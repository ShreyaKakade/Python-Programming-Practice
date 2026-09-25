"""Write a Python program to check Armstrong number."""

num = int(input("Enter a number: "))

upper = len(str(num))
temp_num = num  
sum = 0

while temp_num > 0:
    digit = temp_num % 10
    sum = sum + digit ** upper
    temp_num //= 10

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")