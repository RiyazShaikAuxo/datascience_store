# A function calls itself is a recursion
#A complex task can be broken down into simpler sub-problems using recursion


# Example of recursive fucntion is "Finding a factorial for a number"
def recursivefun(x):
    if x==1:
        return 1
    else:
        return (x*recursivefun(x-1))

x=int(input("Enter any number: "))
print("The Factorial of ", x , "is:",  recursivefun(x))