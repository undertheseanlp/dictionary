import os
from os.path import dirname, exists
from os.path import join

from dictionary import Word, Dictionary

DATA_PATH = join("hongocduc", "raw", "VV")
lines = open(join(DATA_PATH, "vv30K.index")).read().splitlines()[4:]

texts = [line.split("\t")[0] for line in lines]
tmp = []
for text in texts:
    text = Word(text)
    text.set_source("hongocduc")
    tmp.append(text)
words = tmp

dictionary = Dictionary(words)
dictionary.save("dictionary")
