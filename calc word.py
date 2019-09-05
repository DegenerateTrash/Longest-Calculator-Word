import time
wordslist = open("words.txt","r")
badletters = ["F","H","J","K","L","P","Q","T","U","V","W","Z"]
#badletters = ["a","e","i","o","u","."]
wordlists = wordslist.readlines()
longest = ""

#print(wordlists)
#goodletters ABCDEXYMISGRON
start = time.time()
for x in range(0,len(wordlists)-1,1):
    p = 0
    for f in range(0,len(badletters),1):
        if badletters[f].lower() in wordlists[x]:
            p += 1
            
    if p == 0:
        print(wordlists[x].strip())
        if len(wordlists[x])-1 > len(longest):
                longest = wordlists[x]
print("The longest word that can be made without '{0}' is '{1}'".format(",".join(badletters),longest.strip()))
print("Took {0:0.1f} seconds to process {1} words".format(time.time() - start, len(wordlists)))
        
