def birthdayCakeCandles(arr):
    no_of_tall_candles = 1
    key = arr[0]
    for i in range(len(arr)-1):
        if key <= arr[i+1]:
            if key == arr[i+1]:
                no_of_tall_candles = no_of_tall_candles + 1
            key = arr[i+1]

    return no_of_tall_candles  


arr = [3,2,1,3]
birthdayCakeCandles(arr)


            



