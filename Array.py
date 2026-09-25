"Write a Python program to find sum of array"

def sum_array(arr):
    sum = 0
    for num in arr:
        sum = sum + num
    return sum

arr = [1, 2, 3, 4, 5]
result = sum_array(arr)    
print("The sum of the array is:", result)

# arr = [6, 7, 8, 9, 10]
# ans = sum(arr)
# print("The sum of the array is:", ans)