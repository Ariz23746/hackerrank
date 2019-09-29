def sockMerchant(n, ar):
    i = 0
    j = 0
    temp_socks = ar[0]
    pair_socks = {}

    while i < len(ar):
        j = i + 1
        temp_socks = ar[i]
        if temp_socks in pair_socks:
            i+=1
        else:    
            pair_socks[ar[i]] = 1
            while j < len(ar):
                if ar[i] == ar[j]:
                    pair_socks[ar[i]] = pair_socks[ar[i]] + 1
                    j+=1
                else:
                    j+=1
            i+=1

    total_pair_of_socks = 0
    for i in pair_socks:
        if pair_socks[i] > 1:
            total_pair_of_socks = total_pair_of_socks + pair_socks[i] // 2

    return total_pair_of_socks                 
        
n = 9
ar = [10,20,20,10,10,30,50,10,20]
print(sockMerchant(n,ar))