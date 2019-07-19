import numpy as np
a=np.arange(10)
print(a)
b=a
print(b)

#changing the one value in b
b[0]=11
print(b)
#a also changing
print(a)

# to Check whether a,b sharing same momory

samememory=np.shares_memory(a,b)
print(samememory)

# To overcome this we will use copy method

c=np.arange(10)
print(c)
#instead d=c use copy
d=c.copy()
print(d)
d[0]=11
print(c)
print(d)

# to Check whether a,b sharing same momory

samememory=np.shares_memory(c,d)
print(samememory)