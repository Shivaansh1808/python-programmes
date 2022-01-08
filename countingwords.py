userstring = input("Enter Your String: ")
charactercount = 0
wordcount = 1

for i in userstring:
    charactercount = charactercount+1
    
    if i == " ":
        wordcount = wordcount+1
        charactercount = charactercount-1
print(charactercount)
print(wordcount)