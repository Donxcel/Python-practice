import pandas
n = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# alphabets = [i for i in n.letter]
# meaning = [ test  for test in n.code]
# new_dict = {alphabets[i]:meaning[i] for i in range(26)}
#OR: METHOD 2
new_dict = {row.letter:row.code for (index,row) in n.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

get  = input("enter a word ").upper()
# new_word = []
# for i in get:
#    for (key,value) in new_dict.items():
#        if  i == key:
#            new_word.append(value)

#OR
new_word = [new_dict[i] for i in get]
print(new_word)