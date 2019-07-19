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

#Take temp column as my index (Temp will became my index)
var1=df.set_index('temp',inplace=True) #(Inplace=True - Make changes permanently
print(var1)
print(df)

#head to show the top five first columns
datahead=df.head()
print(datahead)

#ILOC STARTS WORKS FROM HERE

# to Show first two columns
res1=df.iloc[[0,1]]
print(res1)

#Get first three reccords and only column "name".

res2=df.iloc[1:3,1]  #Name colmn values not displayed in values because of "1"
print(res2)

#By using boolean values we can get the values
# True takes the serial rows to printing and False skips the rows

res3=df.iloc[[True,True,False,False,True]]
print(res3)

#Get Oth row and alll the columns

res4=df.iloc[0,:]
print(res4)

#Loc only works if list starts from 0th index so we coud not run now instead i will run

res5=df.iloc[1,:]
print(res5)

#get specific indexes using loc

res6=df.loc[[32,66,57]]
print(res6)

#Get 39,84 rows and "name" and "random" names
df.loc[[39,84],'name':r'andom']

# loc with boolean values
df.lo[[True,True,False,True]]

# In dataframe get the "random" where greater than 14
df.loc[df.random>14]

#Docuble condirion using OR
df.loc[(df.random>13 | (df.random==10),:]


