import numpy as np
neye=np.eye(3)
print(neye)
#Fill the matrix with 2
nfull=np.full((3,3),2)
print(nfull)

#Converet interger value instead float value
nintfull=np.full((3,3),2.2,dtype=int)
print(nintfull)

#Diagnal vale matrix
ndiag=np.diag([1,2,3,4,5])
print(ndiag)

#
v=np.array([1,2,3])
ntile=np.tile(v,(3,1))
print(ntile)

ntile2=np.tile(v,(3,2))
print(ntile2)