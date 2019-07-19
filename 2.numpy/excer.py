import numpy as np
a=np.array([[1,2],[3,4]])
sumofa=a.sum()
print(sumofa)
print(a)

#Accesing perticular elements
axsa=a.sum(axis=0)
print(axsa)
axsb=a.sum(axis=1)
print(axsb)

#max element
maxa=a.max()
print(maxa)

#Argmax is tell u at what place it will be max
argma=a.argmax()
print(argma)

#Sort array

sortaray=[1,2,53,3,4,0,2,8,9]
result=np.sort(sortaray)
print(result)
