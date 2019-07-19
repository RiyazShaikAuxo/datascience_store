#Datatable just like a table which contains rows and columns

#Creating a datafrmae in different ways


import numpy as np
import pandas as pd
#Creatig a random value as integer
temp=np.random.randint(low=20, high=100,size=[20,])
name=np.random.choice(['Abhay','Riyaz','Ram','Ashwad'],20)
random=np.random.choice([10,20,30,40,14],20)

#Zip all above
a=list(zip(temp,name,random))

#Creating a data frmae using above data

df=pd.DataFrame(data=a,columns=['temp','name','random'])
print(df)


