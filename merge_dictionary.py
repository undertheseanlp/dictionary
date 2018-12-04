import os
from os import listdir
from os.path import join

from dictionary import Dictionary, DictionaryUtil

DICTIONARIES_FOLDER = "dictionaries"
dirs = [d for d in listdir(DICTIONARIES_FOLDER) if os.path.isdir(join(DICTIONARIES_FOLDER, d))]
dictionaries = []
for dir in dirs:
    path = join("dictionaries", dir)
    dictionary = Dictionary()
    dictionary.load(path)
    dictionaries.append(dictionary)

dictionary = DictionaryUtil.merge(dictionaries)
dictionary.save("dictionary")