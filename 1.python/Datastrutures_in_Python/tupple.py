# tupples once craeted can not be modified at all
#Similar to lists
tuple=(30,'Riyaz',5.8)
print(tuple[0])

tuple1=("Banglore",29.3343,34)
print(tuple1)

#assigning new variable

tuple2=tuple1
print(tuple2)

#tupple not allow item assignment will throw error
    #tuple2(1)="Riyaz"

retrieve1=tuple2[:-1]
print(retrieve1)

#Another way to create a tupple

new_tupple=1,2,3
print(new_tupple)

#Concatinate tupples

cocatinate_tupple=new_tupple,(1,2,3,4,5)
print(cocatinate_tupple)
print(cocatinate_tupple[0])
