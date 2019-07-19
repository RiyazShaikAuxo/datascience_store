# python programm to swap two variables
x=input("Enter the first number: ")
y=input("Enter the second number: ")
temp=x
x=y
y=temp
print("The x value after swapping: {}".format(x))
print("The y value after swapping: {}".format(y))

#Swapping the variable without using temporary variable
x,y=2,3
x,y=y,x
print(x)
print(y)



