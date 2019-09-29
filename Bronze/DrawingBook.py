def pageCount(n, p):
    middle = n / 2
    if p <= middle:
        if p % 2 == 0:
            page_count = p // 2
        else:
            if p == 1:
                page_count = 0
            else:
                page_count = p // 2    

    else:
        if n % 2 == 0:
            if p == n:
                page_count = 0
            else:
                if (n-p) % 2 == 0:
                    page_count = (n-p)//2
                else:
                    page_count = ((n-p)//2) + 1    
        else:
            if p == n or p == n-1:
                page_count = 0
            else:
                page_count = ((n - p) // 2)

                          
    return page_count

n = 10
p = 6

print(pageCount(n,p))