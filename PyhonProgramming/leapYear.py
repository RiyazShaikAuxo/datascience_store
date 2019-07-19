#If the year divisible by 4, 100 and 400 is a leap year elase not a leap year


year=int(input("Enter the year: "))
if (year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is not a leap year")
else:
        print(year, "is not a leap year")
