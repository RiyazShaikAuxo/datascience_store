#for i in range(1,10,3):
    #print(i)



# Example 2

strln=''
for i in range(0,9):
    if i<4:
        strln +='*'
        print(strln)
    elif i>4:
        strln=strln[:-1]
        print(strln)
