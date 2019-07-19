# Program make a simple calculator that can add, subtract, multiply and divide using functions

#This functions adds two numbers
def add(x,y):
    return x+y
#This function multiply two numbers
def multiply(x,y):
    return x*y
#This function Subtract two numbers
def sub(x,y):
    return x-y
#This function Devides two numbers
def devide(x,y):
    return x/y
print("Select the Operations")
print("1. Add")
print("2. Multi")
print("3. SUbract")
print("4. Devides")

#Taking the inputs from the user
choice=input("Enter the choice (1,2,3,4): ")
num1=int(input("Enter the x number: "))
num2=int(input("Enter the y number: "))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"*",num2,"=",multiply(num1,num2))
else:
    print("Invalid Input entered")