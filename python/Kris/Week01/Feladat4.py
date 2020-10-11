sorok_szama = 4
def triangle(n):
    """
    for row in range(sorok_szama):
    print(('{:^'+str(sorok_szama*2-1)+'}').format('*' * (1+row*2)))
    """

    #number of spaces
    spaces = 2*n - 2
    
    #handle number of row
    for row in range(0,n):
        #handle number of space
        for column in range(0, spaces): 
            print(end=" ")

        #decrement spaces
        spaces -= 1

        #handle number of column
        for column in range(0, row + 1):
            print("* ",end="")
        print("")

triangle(sorok_szama)
