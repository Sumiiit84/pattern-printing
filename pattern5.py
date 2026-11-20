# Set the total number of rows
n = 5

# Outer loop controls (from 1 to 5)
for i in range(1, n + 1):
    # Inner loop runs 'i' times to determine how many numbers to print on the current row
    for j in range(1, i + 1):
        # Print the current row number 'i' followed by a space, staying on the same line
        print(i, end=" ")
    # Move to the next line after finishing the current row
    print()