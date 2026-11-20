'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
n = 5
for i in range(1, n + 1):
    if i == 1 or i == n :  # condition meets print *
        print("* " * n)
    else:
        print("* " + "  " * (n-2) + "*")
        
