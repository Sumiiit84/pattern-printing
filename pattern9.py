#of the diamond
n = 5

# First loop prints the top half (upright pyramid from row 1 to 5)
for i in range(1, n + 1):
    # Create decreasing leading doubleto center the stars
    spaces = "  " * (n - i)
    # Create an increasing odd number o stars (1, 3, 5, 7, 9)
    stars = "* " * (2 * i - 1)
    # Combine spaces and stars and print the current row
    print(spaces + stars)

# Second loop prints the bottom half (inverted pyramid from row 4 down to 1, skipping the duplicate middle row)
for i in range(n - 1, 0, -1):
    # Create increasing leading double spaces ("  ") as the rows narrow
    spaces = "  " * (n - i)
    # Create a decreasing odd number of stars (7, 5, 3, 1)
    stars = "* " * (2 * i - 1)
    # Combine spaces and stars and print the current row
    print(spaces + stars)