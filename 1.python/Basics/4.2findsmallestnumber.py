n1=int(input("Enter tge value of n1: "))
n2=int(input("Enter the value of n2: "))
n3=int(input("Enter tge "))
if (n1<=n2 and n1<=n3):
    smallest=n1
elif (n2<=n1 and n2<=n3):
    smallest=n2
else:
    smallest=n3
print("smallest among three numbers is: {}".format(smallest))
