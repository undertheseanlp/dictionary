import json

from dictionary import Word, Dictionary

words = []
for line in open("data/words.txt"):
    word = json.loads(line.strip())
    text = word["text"]
    word = Word(text)
    word.set_source("tudientv")
    words.append(word)
print(len(words))
dictionary = Dictionary(words)
dictionary.save("dictionary")