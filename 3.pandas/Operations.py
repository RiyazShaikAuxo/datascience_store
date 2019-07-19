#Creating DataFrame using dictionaries

import numpy as np
import pandas as pd
#Creatig a random value as integer
temp=np.random.randint(low=20, high=100,size=[20,])
name=np.random.choice(['Abhay','Riyaz','Ram','Ashwad'],20)
random=np.random.choice([10,20,30,40,14],20)
df=pd.DataFrame({'temp':temp,'name':name,'random':random})
print(df)