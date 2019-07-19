import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

#access 1 element
element1=a[0,0]
print(element1)

#accessing 9 element
element2=a[2,2]
print(element2)

#accessing aleemnts greater than 2
element3=a>2
print(element3)

# accesing greter than 2 and less than 5
element4=a[(a>2)&(a<5)]
print(element4)