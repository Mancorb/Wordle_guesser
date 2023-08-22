import re

words =[]

with open("test_one.txt","r",encoding="utf8") as file:
    for line in file:
        if line != "\n" or None:
            word = re.findall('[A-Z]\w*..\B',line)[0]
            word = word[:-2]
            words.append(word)

with open("wordList.txt","a") as file:
    for word in words:
        file.write("\n"+word)

