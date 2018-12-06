from dictionary import Word, Dictionary

texts = open("data/Viet74K.txt").read().splitlines()

tmp = []
for text in texts:
    text = Word(text)
    text.set_source("hongocduc")
    tmp.append(text)
words = tmp

dictionary = Dictionary(words)
dictionary.save("dictionary")
