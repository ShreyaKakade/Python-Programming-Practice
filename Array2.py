"Write a Python Program to find largest element in an array"

def find_largest_element(arr):
    if len(arr) == 0:
        return "Array is empty"

    largest = arr[0]  

    for num in arr:
        if num > largest:
            largest = num  
    return largest

array = [6,2,3,4,5]
result = find_largest_element(array)
print(result)