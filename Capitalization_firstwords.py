input="they're bill's friends from US"
words=input.split(' ')
capitalized_words=[] #took an empty ro collect all the capitalised words and to add them at the end
for word in words:
    title_case_word=word[0].upper() +word[1:]
    capitalized_words.append(title_case_word)
output=' '.join(capitalized_words)
print(output)