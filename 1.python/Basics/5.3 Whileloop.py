num=int(input("Enter any number to find whether it is prime or not: "))
isDivisible=False;
i=2;
while num%i==0:
    isDivisible=True;
    print("{} is divisible by {}: ".format(num,i))
    i+=1;
if isDivisible:
    print("{} is not a prime number".format(num))
else:
    print("{} is a prime number".format(num))