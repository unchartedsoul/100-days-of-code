import pandas

new_file = pandas.read_csv("nato_phonetic_alphabet.csv")
word_nato ={row.letter:row.code for (letter,row) in new_file.iterrows()}

name = input("enter the name").upper()
word = [word_nato[letter] for letter in name]
print(word)
