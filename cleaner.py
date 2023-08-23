import re
import os
words = []


with open("wordlist_esp.txt", "r") as file:
    for line in file:
        if line != "\n":
            res = re.findall("[^0-9,.\n]",line)
            word=""
            for i in res:
                word=word+i
            words.append(word.strip())

print("+\tData extracted")

with open("wordlist_esp_.txt","w") as file:
    for i in words:
        file.write(i+"\n")
print("+\tProcess finnished")