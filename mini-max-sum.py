def MinMaxSum(arr):
    i = 0
    
    m = len(arr) - 1
    while i < len(arr)-1:
        j = 0
        while j < m:
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp   
            j+=1     
        i=i+1
        m = m - 1
               
                   

    lsum_list = []
    rsum_list = []
    sum_list = []
    temp_l = 0
    temp_r = 0
    i = 0
    j = 1
    k = j
    t = 0
    m = len(arr) - 1
    while i < len(arr):
        j = k
        while j < len(arr):
            temp_r = temp_r + arr[j]
            j+=1
            if j == 5:
                j = 1
                rsum_list.append(temp_r) 
                temp_r = 0
                break
        while t < m:
            temp_l = temp_l + arr[t]
            t+=1
            if t == m:
                lsum_list.append(temp_l) 
                temp_l = 0 
                t = 0
                break      
        k = k + 1
        i = i + 1
        m = m - 1

    
    
    temp = rsum_list[0]
    sum_list.append(temp)
    temp = lsum_list[0]
    sum_list.append(temp)
    j = 1
    i = len(arr) - 2
    while True:
        sum = 0
        sum = rsum_list[j] + lsum_list[i]
        #print(sum)
        sum_list.append(sum)
        j = j + 1
        i = i - 1
        if j == len(arr) - 1:
            break
           

    i = 0
    j = 1
       

    print(sum_list[1],end=" ")
    print(sum_list[0])    

    
   
    

arr = [769082435,210437958,673982045,375809214,380564127]
#arr = [1,2,3,4,5]
#arr = [14,10,13,12,11]
MinMaxSum(arr)
            


        