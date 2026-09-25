"""Write a Python Program to find Armstrong number in an interval."""

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range:"))

for num in range(lower, upper + 1):
 order = len(str(num))
 sum = 0
 temp_num = num
 
 while temp_num > 0:
    digit = temp_num % 10
    sum = sum + digit ** order 
    temp_num //= 10
    
 if num == sum:
        print(num)
    