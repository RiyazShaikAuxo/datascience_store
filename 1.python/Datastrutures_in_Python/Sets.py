# to get the unique element out of a collection
# to find common element in various collections
lists=['A','B','C','D','A','C']

#Convert my lsit to SET

set1=set(lists)
print(set1)
set2={'A','B'}

#intersection
print(set1.intersection(set2))
#union
print(set1.union(set2))
#difference
print(set1.difference(set2))

# in function
res='A' in set2
print(res)

#add value to set
set2.add("G")
print(set2)

#remove velure
set2.remove("G")
print(set2)

#for loop
for set4 in set1:
    print(set4)

for set5 in set2:
        print(set5)