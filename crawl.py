import json
import os
from os.path import exists

import requests
from bs4 import BeautifulSoup

output_filepath = "data/words.txt"
if exists(output_filepath):
    os.remove(output_filepath)
output_file = open(output_filepath, "a")
characters = "A Ă Â B C D Đ E Ê G H I K L M N O Ô Ơ P Q R S T U Ư V X Y".split()
for character in characters:
    url = f"http://tudientv.com/browse.php?l={character}"
    r = requests.get(url)

    for page in range(1, 100):
        try:
            url = f"http://tudientv.com/browse.php?l={character}&p={page}"
            r = requests.get(url)
            html = r.content.decode("utf-8")
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.select("ul li")
            if len(tags) > 0:
                for tag in tags:
                    a = tag.select_one("a")
                    href = a.attrs["href"]
                    text = str(a.string)
                    content = {"url": href, "text": text}
                    content = json.dumps(content, ensure_ascii=False)
                    output_file.write(f"{content}\n")
                print(f"Success {url}")
            else:
                break
        except Exception as e:
            print(e)
