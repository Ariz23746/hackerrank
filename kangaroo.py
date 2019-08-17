def kangaroo(x1, v1, x2, v2):
    if v1 == 0 and v2 == 0:
        print("NO")
    else:
        t = (x2 - x1)/(v1-v2)

        if t < 0:
            print("NO")
        else:
            print("YES")

x1 = 0
x2 = 5
v1 = 2
v2 = 3
kangaroo(x1,v1,x2,v2)           