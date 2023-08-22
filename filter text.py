lines=[]
counter = 0
with open("wordList.txt","r") as file:
    
    for line in file:
        counter= counter +1
        lines.append(line[:-1])

with open("wordList_1.txt","w") as file:
    for line in lines:
        file.write(line+"\n")