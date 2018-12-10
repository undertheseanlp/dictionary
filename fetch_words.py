from os import remove
from os.path import exists

import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def fetch(url):
    r = requests.get(url)
    html = r.content.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    words = soup.select("#mw-pages .mw-category-group ul li a")
    words = [word.text for word in words]
    next_tags = soup.select('#mw-pages a[title="Thể loại:Mục từ tiếng Việt"]')
    next_url = None
    for tag in next_tags:
        if tag.text == 'Trang sau':
            next_url = "https://vi.wiktionary.org" + tag.attrs["href"]
            break
    return words, next_url

url = "https://vi.wiktionary.org/wiki/Th%E1%BB%83_lo%E1%BA%A1i:M%E1%BB%A5c_t%E1%BB%AB_ti%E1%BA%BFng_Vi%E1%BB%87t"
total = 0

OUTPUT_FILEPATH = "tmp/words.txt"
if exists(OUTPUT_FILEPATH):
    remove(OUTPUT_FILEPATH)
OUTPUT_FILE = open("tmp/words.txt", "a")

while True:
    print(unquote(url))
    words, url = fetch(url)
    total += len(words)
    print(f"{len(words)}/{total}")
    content = "\n".join(words) + "\n"
    OUTPUT_FILE.write(content)
    # if total > 500:
    #     break
    if url is None:
        break