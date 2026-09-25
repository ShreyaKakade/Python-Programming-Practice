"""Write a Python program to find the sum of Natural Numbers."""

limit = int(input("Enter the limit: "))

sum = 0

for num in range(1, limit + 1):
    sum = sum + num
    
print(sum)
