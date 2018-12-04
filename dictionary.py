import json
import os
from os.path import join, exists


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
            content = {"text": word.text, "source": word.source}
            content = json.dumps(content, ensure_ascii=False)
            f.write(content + "\n")
