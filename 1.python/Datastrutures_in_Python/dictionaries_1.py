d={'actor':'amir','sachin':'cricketer','biscut':2,"list":[12,23,22]}
print(d)
actor1=d['actor']
print(actor1)

#get list form dictionaries
age=d.get('list')
print(age)


#Assign dictionaries
d['biscut']=3
print(d)
# addd value to dic
d['run']='away'
print(d)

# get list of keys
print(d.keys())
print(d.values())
# deletion
del d['actor']

#len
print(len(d))

print(d)

#for loop
for a,b in d.items():
    print(a,b)