def birthday(s, d, m):
    if m == 1:
        if len(s) == 1:
            if s[0] == d:
                return 1
            else:
                return 0
        else:
            new_list = []
            i = 0
            while i < len(s):
                if s[i] == d:
                    new_list.append(s[i])
                i+=1
            return len(new_list)            
   

    else:        
        new_list = []
        i = 0
        temp = 0
        mfork = m
        while i <= (len(s) - m):
            k = i
            temp_list = []
            temp = 0
            while k < mfork:
                temp_list.append(s[k])
                temp = temp + s[k]
                k+=1      
            if temp == d:
                new_list.append(temp_list)
            i+=1
            mfork+=1
        return len(new_list)        

s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
d = 18
m = 7
print(birthday(s,d,m))    