languages=["Java","C++","Python","Scala",42]
print(languages)
print(languages[0])
print(languages[1:3])
print(languages[-2])
print(languages[1:])
print(languages[:-2])
# add value
languages.append("ML")
print(languages)

# Pop: Taking out the last element in it and remove
pop1=languages.pop()
print(pop1)
print(languages)
pop2=languages.pop(1)
print(pop2)
print(languages)