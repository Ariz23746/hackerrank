def getMoneySpent(keyboards, drives, b):
    i = 0
    temp1 = 0
    inBudget = []

    while i < len(keyboards):
        j = 0
        temp1 = keyboards[i]
        while j < len(drives):
            temp1 += drives[j]
            if temp1 <= b:
                inBudget.append(temp1)   
            temp1 = keyboards[i]    
            j+=1
        i+=1
    print(inBudget)        
    if len(inBudget) == 0:
        temp = -1
        return temp
    else:    
        i = 1
        temp = inBudget[0]
        while i < len(inBudget):
            if temp < inBudget[i]:
                temp = inBudget[i]
                i+=1
            else:
                i+=1
        return temp                


keyboards = [3,1]
drives = [5,2,8]
budget = 10
print(getMoneySpent(keyboards,drives,budget))