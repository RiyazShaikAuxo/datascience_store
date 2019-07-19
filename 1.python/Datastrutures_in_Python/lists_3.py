mail="Hi Riyaz, you are doing a good job. keep it up."

# Space delemeter
words=mail.split()
print(words)

# . Delemeter

words1=mail.split('.')
print(words1)

#Join delemetet

words2=".".join(words1)
print(words2)

#multiply string

list1=["Riyaz"]
print(list1*6)

# Lenth of the list
print(list1+list1)
print(len(list1))

num=[2,6,9,3,2,10]
print(num[1::2])

#sort number
print(sorted(num))


#max function
print(max(num))

#Min fucntion

print(min(num))

#Creating a composite list in lists

compositelist=[[1,2,4],[4,3,2],[4,7,9]]
print(compositelist[1])
# zeroth index
print(compositelist[0][1])
print(compositelist[0][0])
print(compositelist[0][2])