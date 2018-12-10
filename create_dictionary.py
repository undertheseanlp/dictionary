from dictionary import Dictionary, Word



words = []
for text in open("tmp/words.txt"):
    word = Word(text.strip())
    word.set_source("wiktionary")
    words.append(word)

dictionary = Dictionary(words)
dictionary.save("dictionary")