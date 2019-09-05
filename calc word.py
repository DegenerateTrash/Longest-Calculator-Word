wordslist = open("words.txt","r")
badletters = ["F","H","J","K","L","P","Q","T","U","V","W","Z"]
#badletters = ["a","e","i","o","u","."]
wordlists = wordslist.readlines()
longest = ""
#print(wordlists)
#goodletters ABCDEXYMISGRON

for x in range(0,len(wordlists)-1,1):
    p = 0
    for f in range(0,len(badletters)-1,1):
        if badletters[f].lower() in wordlists[x]:
            p += 1
            
    if p == 0:
        print(wordlists[x].strip())
        if len(wordlists[x])-1 > len(longest):
                longest = wordlists[x]
print(longest.strip())
        
