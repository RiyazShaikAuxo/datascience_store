x=int(input("Enter eny number: "))
if (x%2==0):
    print(x, "is not a prime number")
else:
    print(x, "is a prime number")



    #   OR
num=int(input("Enter any number: "))
if num>1:
    for i in range(2, num):
        if (num%i)==0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
        else:
            print(num, "Is a prime number")
    else:
        print(num, "is not a prime number")
