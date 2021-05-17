import json
from difflib import get_close_matches
data = json.load(open("data.json"))

# function


def findMeaning(word):
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:

        print(
            f'did u mean {get_close_matches(word,data.keys())[0]}\nif yes type "Y" no type "N"')
        inp = input().lower()
        if inp == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return f'sorry {word} word not available in our database'
    else:
        return 'sorry i did not understand ur language'


# user input
word = input("what word you want meaning: ").lower()
output = findMeaning(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)


