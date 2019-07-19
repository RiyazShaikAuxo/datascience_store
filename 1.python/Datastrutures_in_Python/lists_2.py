languages=["Java","C++","Python","Scala",42]
languages.append("ML")
print(languages)
languages.remove("ML")
print(languages)

# ID memory loation
print(id(languages))
new_list=languages[:]
print(id(new_list))
another_list=new_list.copy()
print(id(another_list))