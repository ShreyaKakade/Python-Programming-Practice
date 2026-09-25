"""Write a Python Program to print all Prime numbers in an interval of 1-10."""
lower = 1
upper = 10

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)