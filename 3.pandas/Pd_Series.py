# Create pandas series
import pandas as pd
a=pd.Series([1,2,3,4,5])
print(a)

#retrieve the values
b=pd.Series(['A','B','C','D'])
print(b)

#print date range using range funtion like in numpy
dater=pd.date_range(start='01-01-2019',end='10-01-2019')
print(dater)