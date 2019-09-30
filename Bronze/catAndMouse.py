def catAndMouse(x, y, z):
    if x > z:
        if y > z:
            if (x-z) > (y-z):
                return 'Cat B'
            elif (x-z) < (y-z):
                return 'Cat A'
            else:
                return 'Mouse C'
        else:
            if (x-z) > (z-y):
                return 'Cat B'
            elif (x-z) < (z-y):
                return 'Cat A'
            else:
                return 'Mouse C'
    else:
        if y > z:
            if (z-x) > (y-z):
                return 'Cat B'
            elif (z-x) < (y-z):
                return 'Cat A'
            else:
                return 'Mouse C'    
        else:
            if (z-x) > (z-y):
                return 'Cat B'
            elif (z-x) < (z-y):
                return 'Cat A'    
            else:
                return 'Mouse C'
                
x = 1
y = 2
z = 3
print(catAndMouse(x,y,z))