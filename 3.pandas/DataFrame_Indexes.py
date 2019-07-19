import numpy as np
import pandas as pd
#Creatig a random value as integer
temp=np.random.randint(low=20, high=100,size=[20,])
name=np.random.choice(['Abhay','Riyaz','Ram','Ashwad'],20)
random=np.random.choice([10,20,30,40,14],20)
df=pd.DataFrame({'temp':temp,'name':name,'random':random})
print(df)

#Take temp column as my index (Temp will became my index)
var1=df.set_index('temp',inplace=True) #(Inplace=True - Make changes permanently
print(var1)
print(df)

#Sort in decending Order
sorddata=df.sort_index(axis=0, ascending=False)
print(sorddata)

#Sort values randomly
var2=df.sort_values(by='random',ascending=False)
print(var2)

#Drop the column
#Droping random for the table df

var3=df.drop(['random'],axis=1)
print(var3)

#Check df
print(df)

#If you want delete random column permamntly use inplace=True

var4=df.drop('random',inplace=True)
print(var4)