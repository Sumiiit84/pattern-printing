# Set the number of rows for the top half (widest point) of the butterfly
n = 5

# First loop prints the top half (rows 1 to 5, expanding toward the center)
for i in range(1, n + 1):
    # Create the left wing with 'i' stars
    left = "* " * i
    # Create the shrinking gap of double spaces ("  ") between the two wings
    spaces = "  " * (2 * (n - i))
    # Create the right wing with 'i' stars
    right = "* " * i
    # Combine left wing, center spaces, and right wing and print the row
    print(left + spaces + right)

# Second loop prints the bottom half (rows 4 down to 1, skipping the duplicate middle row)
for i in range(n - 1, 0, -1):
    # Create the shrinking left wing with 'i' stars
    left = "* " * i
    # Create the widening gap of double spaces ("  ") between the two wings
    spaces = "  " * (2 * (n - i))
    # Create the shrinking right wing with 'i' stars
    right = "* " * i
    # Combine left wing, center spaces, and right wing and print the row
    print(left + spaces + right)