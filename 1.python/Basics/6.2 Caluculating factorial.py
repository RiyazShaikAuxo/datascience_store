#5!=5*4*3*2*1

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return n

fac=factorial(4)
print(fac)