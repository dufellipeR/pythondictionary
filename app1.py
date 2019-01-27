import json
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("data.json"))

user = input("Palavra a ser buscada: ").lower()

try:
    ls = data[user]
    for i in ls:
        print(i)
except:
    wd = get_close_matches(user, data.keys())
    wd = wd[0]
    j = input("Você quis dizer " + wd + "? Se sim (Y) se não (N): ").lower()
    if j == "y":
        ls = data[wd]
        for i in ls:
            print(i)
    else:
        print("Tal palavra não condiz com o real !")
        print("Escreva uma palavra existente !")
