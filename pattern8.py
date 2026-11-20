# Set the total number of rows for the inverted pyramid
n = 5

# Loop backward from n (5) down to 1 so 'i' decreases by 1 each row
for i in range(n, 0, -1):
    # Create leading double spaces ("  ") that increase as 'i' gets smaller
    spaces = "  " * (n - i)
    # Create a decreasing odd number of stars (9, 7, 5, 3, 1) for the current row
    stars = "* " * (2 * i - 1)
    # Combine the spaces and stars and print the completed row
    print(spaces + stars)