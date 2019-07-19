# pgrm to print pattern

#*
#* *
#* * *
#* * * *
#* * * * *


num=int(input("Enter the number of choices to print the numbers: "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()