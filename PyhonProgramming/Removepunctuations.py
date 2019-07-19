# '''!()-[]{};:'"\,<>./?@#$%^&*_~''' (There are the punctuations)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_strng="Hello----__ my(),; World"
no_punct=""
for char in my_strng:
    if char not in punctuations:
        no_punct=no_punct+char
print(no_punct)


