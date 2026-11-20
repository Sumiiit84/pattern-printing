# Set the total number of rows 
n = 5

# Outer loop controls the current row number 
for i in range(1, n + 1):
    # Inner loop prints numbers starting from 1 up to the row number 'i'
    for j in range(1, i + 1):
        # Print the current number followed by a space, staying on the same line
        print(j, end=" ")
    # Move to the next line after finishing all numbers for the current row
    print()