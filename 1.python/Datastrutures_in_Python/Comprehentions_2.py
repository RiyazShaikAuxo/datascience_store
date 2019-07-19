# list comp with if statements
paragraph="There was a fax.", 'It was brown in color.', "It was seen near that farm sometime back."
vowels=['a','e','i','o','u']
vowels_from_sentence=[]
for sentence in paragraph:
    for word in sentence.split():
        if word[0].lower() in vowels:
            vowels_from_sentence.append(word)
print(vowels_from_sentence)

#OR
vowels_from_sentence=[word for sentence in paragraph for word in sentence.split() if word(0).lower() in vowels]
print(vowels_from_sentence)