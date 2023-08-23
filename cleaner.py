import re

words = []
end = False
loc="new.txt"

with open(loc, "r", encoding="utf8") as file: # utf8 for special characters
    for line in file:
        if line != "\n":
            res = re.findall("[^0-9,.\n]",line)# Delete all numbers and spaces
            word=""
            for i in res: #join all found matches
                if i =="/": # sparate cases like "lustro / dias" to get just one and continue withouth adding the "/"
                    words.append(word.strip())
                    word=""
                if i =="\t":
                    words.append(word.strip())
                    end = not end
                    break
                else:
                    word=word+i
            if not end:
                words.append(word.strip())
            else:
                end = not end

print("[+] Data extracted")

with open("wordlist_esp.txt","a", encoding="utf8") as file:
    for i in words:
        file.write("\n"+i)
print("[+] Process finnished")