# Set the total number of rows for the pyramid
n = 5

# Loop from 1 up to n (inclusive) so 'i' represents the current row number
for i in range(1, n + 1):
    # Create leading double spaces ("  ") to push the stars toward the center
    spaces = "  " * (n - i)
    # Create an odd number of stars (1, 3, 5, 7, 9) for the current row
    stars = "* " * (2 * i - 1)
    # Combine the spaces and stars and print the completed row
    print(spaces + stars)