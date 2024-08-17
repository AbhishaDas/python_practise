def input_2d_array(rows, cols):
    array = []
    print(f"Enter {rows} rows and {cols} columns:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at [{i}][{j}]: "))
            row.append(element)
        array.append(row)
    return array

def sum_2d_arrays(arr1, arr2):
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        print("Error: Arrays must have the same dimensions.")
        return None
    
    sum_array = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        sum_array.append(row)
    return sum_array

# Input dimensions of the arrays
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input the first 2D array
print("\nEnter elements of first array:")
array1 = input_2d_array(rows, cols)

# Input the second 2D array
print("\nEnter elements of second array:")
array2 = input_2d_array(rows, cols)

# Compute the sum of the arrays
sum_array = sum_2d_arrays(array1, array2)

# Display the sum array
if sum_array:
    print("\nSum of the two arrays:")
    for row in sum_array:
        print(row)