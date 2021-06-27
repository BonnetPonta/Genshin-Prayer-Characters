# https://h1g.jp/genshin/?過去のガチャ情報
from pprint import pprint
from collections import Counter
from json import load

# g は gatya　の略
with open(r"DB.json", "r", encoding="utf-8_sig") as f:
    json_load = load(f)
characters = [elems[i] for i in range(4) for elems in json_load.values()]

pprint(Counter(characters))
