import numpy as np
a=np.linspace(1,50,100)
print(a)

#Find item size

itemsize=a.itemsize
print(itemsize)

#Change shape on range
cshape=np.arange(18).shape
print(cshape)

#Reshape matrix
cmatrix=np.arange(18).reshape(2,3,3)
print(cmatrix)
cmatrix.shape