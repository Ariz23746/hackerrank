def birthdayCakeCandles(arr):
    greater = []
    j = 1
    key = arr[0]
    for i in range(len(arr)-1):
        if key <= arr[i+1]:
            if key == arr[i+1]:
                j = j + 1
            key = arr[i+1]
            greater.append(key)

    print(greater)
    print(j)   


arr = [3,2,1,3]
birthdayCakeCandles(arr)


            



