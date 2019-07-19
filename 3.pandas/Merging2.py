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

df=pd.merge(d1,d2,on='city')
print(df)

#Perform join
df2=pd.merge(d1,d2,on='city',how='outer')
print(d2)