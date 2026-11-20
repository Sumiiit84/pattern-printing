# Set the total number of rows for the hollow triangle
n = 5

# Loop from 1 up to n (inclusive) so 'i' represents the current row number
for i in range(1, n + 1):
    # First row: print a single star at the top vertex
    if i == 1:
        print("*")
    # Last row: print a solid base of 'n' stars separated by spaces
    elif i == n:
        print("* " * n)
    # Middle rows: print a border star, inner hollow spaces, and an
    else:
        print("* " + "  " * (i - 2) + "*")