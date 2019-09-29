def bonAppetit(bill, k, b):
    actual_bill = 0
    i = 0
    while i < len(bill):
        if i == k:
            i+=1
        else:
            actual_bill = actual_bill + bill[i]
            i+=1
    actual_bill = actual_bill // 2
    if actual_bill == b:
        print("Bon Appetit")

    else:
        print(b - actual_bill)                


n = 4
k = 1
bill = [3,10,2,9]
b = 12

bonAppetit(bill,k,b)