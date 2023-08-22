import re

words =[]

with open("test_one.txt","r") as file:
    lines = file.readlines()

    for line in lines:
        word = re.findall('[A-Z]\w* \B',line)
        word.replace(" ","")
        words.append(word)

with open("wordList.txt","a") as file:
    for word in words:
        file.write("\n"+word)

