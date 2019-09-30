def countingValleys(n, s):
    i = 0
    valley = 0
    current_position = 0

    while i < len(s):
        if s[i] == 'D':
            current_position-=1
           
        if s[i] == 'U':
            current_position+=1

        if current_position == 0 and s[i] == 'U':
            valley += 1
        i+=1       
    return valley

n = 8
s=['U','D','D','D','U','D','U','U']
print(countingValleys(n,s))