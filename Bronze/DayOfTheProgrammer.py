import datetime
def dayofProgrammer(year):
    jan = 31
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    sept = 30
    oct = 31
    nov = 30
    dec = 31
    target_sum = 256
    
    if year > 1918:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            feb = 29
        else:
            feb = 28

    elif year < 1918:
        if year % 4 == 0:
            feb = 29
        else:
            feb = 28
    else:
        feb = 15        
    year_array = [jan,feb,march,april,may,june,july,august,sept,oct,nov,dec]
    temp = 0
    i = 0

    while i < len(year_array):
        if temp < target_sum:
            previous_temp = temp
            temp = temp + year_array[i]
        else:
            break
        i+=1


    date = target_sum - previous_temp
    x = datetime.datetime(year, i, date)
    print(x.strftime('%d.%m.%Y'))

    
year = 1800
dayofProgrammer(year)





                
