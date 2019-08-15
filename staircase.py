# Complete the staircase function below.
def staircase(n):
    i = 0
    j = 0
    while i < n:
        j = i
        k = 0
        while j < n:
            print(" ", end='')
            j = j + 1
        while k <= i:    
            print("#", end='')
            k = k + 1    
        print("\t")    
        i = i + 1    


n = int(input("Enter the height of staircase: "))
staircase(n)        