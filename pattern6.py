# Set the total number o
n = 5

# Loop from 1 up to n  represents the current row number
for i in range(1, n + 1):
    # Print leading  to push the stars to the right, followed by 'i' stars ("* ")
    print("  " * (n - i) + "* " * i)