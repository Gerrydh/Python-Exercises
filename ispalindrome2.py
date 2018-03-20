#IS the word a palidrome
# aka is the word spelt the same backwards as forwards

wrd=input("Please enter a word: ")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print ("This word is palidrome")
else:
    print ("This word is not a palidrome")
