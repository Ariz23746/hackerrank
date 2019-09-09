def divisibleSumPairs(n, k, ar):
    i = 0
    j = 0
    new_list = []
    while i < len(ar):
        j = i + 1
        temp_list = []
        temp = ar[i]
        while j < len(ar):
            temp = temp + ar[j]
            if temp % k == 0:
                temp_list.append(ar[i])
                temp_list.append(ar[j])
                new_list.append(temp_list)
                temp_list = []
            temp = ar[i]
            j+=1
        i+=1
        
    # print(new_list)
    return len(new_list)        

n = 6
k = 3
ar = [1,3,2,6,1,2]
print(divisibleSumPairs(n,k,ar))
