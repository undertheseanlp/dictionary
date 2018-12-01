import os
from os.path import dirname, exists
from os.path import join

class Word:
    def __init__(self, text):
        self.text = text

    def set_source(self, source):
        self.source = source

class Dictionary:
    def __init__(self, words):
        self.words = words

    def save(self, dictionary_path):
        file = join(dictionary_path, "A.txt")
        if exists(file):
            os.remove(file)
        f = open(file, "a")
        for word in self.words:
            f.write(word.text + "\n")

ROOT_PATH = dirname(dirname(__file__))
DATA_PATH = join(ROOT_PATH, "data", "hongocduc", "raw", "VV")
lines = open(join(DATA_PATH, "vv30K.index")).read().splitlines()[4:]

DICTIONARY_PATH = join(ROOT_PATH, "dictionary")
texts = [line.split("\t")[0] for line in lines]
tmp = []
for text in texts:
    text = Word(text)
    text.set_source("hongocduc")
    tmp.append(text)
words = tmp

dictionary = Dictionary(words)
dictionary.save(DICTIONARY_PATH)
