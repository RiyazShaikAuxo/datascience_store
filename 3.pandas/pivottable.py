#Same like groupby

import pandas as pd
d1=pd.DataFrame({
    "city":["Nellore","Hy","Chennai"],
    "Whether":[29,35,45]
})
print(d1)

d2=pd.DataFrame({
    "city":["Ban","hyd","chennai"],
    "humidity":[23,34,54]
})
print(d2)

#Pivot table ex
df=d1.pivot_table(values='whether',index='city',aggfunc='mean')
print(df)

df2=