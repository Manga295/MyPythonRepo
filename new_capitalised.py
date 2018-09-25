
def toJadenCase(string):
    individual_words=string.split(' ')
    capitalised_words=[]
    for word in individual_words:
        title_caseword=individual_words[0].upper()+individual_words[1:]
        capitalised_words.append(title_caseword)
        output=' '.join(capitalised_words)
        print(output)
toJadenCase("they're bill's friends from US")