def countApplesAndOranges(s, t, a, b, apples, oranges):
    no_of_apples = 0
    no_of_oranges = 0
    range_list = []
    if len(apples) >= len(oranges):
        breakstatement = len(apples)
    else:
        breakstatement = len(oranges)    


    while s <= t:
        range_list.append(s)
        s = s + 1
      
        
    i = 0
    
    while i < len(apples):
        apples[i] = apples[i] + a
        i+=1

    i=0
    while i < len(oranges):    
        oranges[i] = oranges[i] + b
        i+=1
        
    
    i = 0
    while True:
        if i == breakstatement:
            break
        else:
            k = 0
            while k < len(range_list):
                if i < len(apples):
                    if apples[i] == range_list[k]:
                        no_of_apples = no_of_apples + 1
                if i < len(oranges):        
                    if oranges[i] == range_list[k]:
                        no_of_oranges = no_of_oranges + 1    
                k+=1    
        i+=1    

    print(no_of_apples)
    print(no_of_oranges)


    # k = 0
    # i = 0
    # while i < len(apples):
    #     k = 0
    #     while k < len(range_list):
    #         if apples[i] ==  range_list[k]:
    #             no_of_apples+=1
    #         k+=1
    #     i+=1

    # k = 0
    # i = 0
    # while i < len(oranges):
    #     k = 0
    #     while k < len(range_list):
    #         if oranges[i] ==  range_list[k]:
    #             no_of_oranges+=1
    #         k+=1
    #     i+=1                 

    # print(no_of_apples)
    # print(no_of_oranges)

s = 7
t = 10
a = 4
b = 12
apples = [2,3,-4]
oranges = [3,-2,-4]
countApplesAndOranges(s, t, a, b, apples, oranges)
        