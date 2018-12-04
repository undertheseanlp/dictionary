from dictionary import Dictionary
import pandas as pd

dictionary = Dictionary()
dictionary.load("dictionary")

sources = []
for word in dictionary.words:
    sources.append(" ".join(word.source))

s = pd.Series(sources)
print(s.describe())
print(s.value_counts())
print(0)