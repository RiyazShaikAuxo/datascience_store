# Merging & Contact

import pandas as pd
import numpy as np
data1=pd.DataFrame([['a',1],['b',2]],columns=['Coll','Number'])
data2=pd.DataFrame([['c',3,'Lion'],['d',4,'Tiger']],columns=['Letter','Number','Animal'])
print(data1)
print(data2)

#Concatinate data frames by row wise

df1=pd.concat([data1,data2],axis=0)
print(df1)

#Ignore index
df1=pd.concat([data1,data2],axis=0,ignore_index=True)
print(df1)


#Concatinaate respect to the y-axis
df2=pd.concat([data1,data2],axis=1)
print("Print for Y-axis")
print(df2)