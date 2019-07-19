paragraph="There was a fax.", 'It was brown in color.', "It was seen near that farm sometime back."

single_wordlist=[]
for sentence in paragraph:
    for word in sentence.split():
        single_wordlist.append(word)

print(single_wordlist)


#OR
single_wordlist=[word for sentence in paragraph for word in sentence.split()]
print(single_wordlist)