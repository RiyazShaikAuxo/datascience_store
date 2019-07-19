import numpy as np
a=np.array([2,4,6,8,10,12,14,16])
print(a)

# Taking 2nd element
element1=a[1]
print(element1)

#Printing 6 element
element2=a[2]
print(element2)

#Accesing 6,10,14
element3=a[[2,4,6]]
print(element3)

# From index 2 to all elements

element4=a[2:]
print(element4)

#accesing for 2 to 5

element5=a[2:5]
print(element5)

# Jump 2

element6=a[0::2]
print(element6)