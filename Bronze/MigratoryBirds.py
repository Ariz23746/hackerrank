def migratoryBirds(arr):
    type1 = 0
    type2 = 0
    type3 = 0
    type4 = 0
    type5 = 0
    list = []

    for i in arr:
        if i == 1:
            type1+=1
        elif i == 2:
            type2+=1
        elif i == 3:
            type3+=1
        elif i == 4:
            type4+=1
        elif i == 5:
            type5+=1

    list.append(type1)
    list.append(type2)
    list.append(type3)
    list.append(type4)
    list.append(type5)
    print(list)
    i = 0
    temp = list[0]
    while i < (len(list) - 1):
        if temp <= list[i+1]:
            if temp == list[i+1]:
                currentindex = i+1
            else:
                temp = list[i+1]
                currentindex = i+2    
                
        i+=1       
    return currentindex

arr = [1,2,3,4,5,4,3,2,1,3,4]
arr2 = [1,4,4,4,5,3]
print(migratoryBirds(arr2))