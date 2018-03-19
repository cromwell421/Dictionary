

import json
from difflib import get_close_matches
data = json.load(open("data.json","r"))


def dictionary(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data.keys())) > 0:
        close = input("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        close = close.lower()
        if close == "y" or close == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif close == "n" or close == "no":
            return "%s not defined. Please double check it." % word
        else: return "We do not understand your response..."
    else:
        return "Word not defined. Please double check it."

word = input("Enter word: ")
output = dictionary(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
