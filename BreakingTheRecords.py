def breakingRecords(scores):
    min = 0
    max = 0
    max_scores = scores[0]
    min_scores = scores[0]

    i=1
    while i < len(scores):
        if scores[i] > max_scores:
                max_scores = scores[i]    
                max = max + 1
        if scores[i] < min_scores :
            min_scores = scores[i] 
            min = min + 1
        i+=1    

    print(max,end=" ")
    print(min)            

scores = [3,4,21,36,10,28,35,5,24,42]
breakingRecords(scores)