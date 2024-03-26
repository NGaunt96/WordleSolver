from random import *

def findScore(l, word):
   score = 0
   for char in word:
      score += l.index(char.lower())
   return score

def findBestWord(bestword, bestscore, correctchars, wrongchars, wrongpos, correctpos):
   for w in wordlist:
      word = w.lower()
      validchars = 0
      correctcount = 0
      chars = []
      for character in word:
         char = character.lower()
         if char in wrongchars:
            validchars = -1
         elif char in chars:
            validchars = -1
         else:
            if word.find(char) in wrongpos[char]:
               validchars = -1
            else:
               if char in correctpos:
                  if word.find(char) == correctpos[char]:
                     validchars += 1
                     correctcount += 1
               elif char in correctchars:
                  validchars += 1
                  correctcount += 1
               else:
                  validchars += 1
                  

                     
         chars.append(char)
         
      if correctcount == len(correctchars) and validchars == 5 and scores[word] > bestscore:
         bestword = word.lower()
         bestscore = scores[word]
         
   return bestword

#initialize
wordlist = []
scores = {}
bestword = ""
bestscore = 0
correctchars = []
answer = 'no'
wrongchars = []
wrongpos = {}
correctpos = {}
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lettercount = {}
poscount = {}


for i in range(26):
   lettercount[letters[i].lower()] = 0
   poscount[letters[i].lower()] = {0: 0, 1: 0, 2: 0, 3:0, 4: 0}
with open("5 Letter Word List.txt", "r") as f:
   for line in f:
      wordlist.append(line.strip().lower())
for i in wordlist:
   for char in i:
      lettercount[char.lower()] += 1
      poscount[char.lower()][i.find(char.lower())] += 1

orderedletters = {k: v for k, v in sorted(lettercount.items(), key=lambda item: item[1])}
bestletters = list(orderedletters)
      
for i in wordlist:
   word = i.lower()
   scores[word] = findScore(bestletters, word)


for letter in letters:
   wrongpos[letter.lower()] = []
   
rightpos = {}
while answer.lower() != 'yes':
   bestword = findBestWord(bestword, bestscore, correctchars, wrongchars, wrongpos, correctpos).lower()
   print(bestword)
   while input("Valid word? ").lower() == "no":
      with open("5 Letter Word List.txt", "r") as f:
         lines = f.readlines()
      with open("5 Letter Word List.txt", "w") as f:
         for line in lines:
            if line.strip("\n") != bestword.lower():
               f.write(line.lower())
      wordlist.remove(bestword)
      bestword = findBestWord(bestword, bestscore, correctchars, wrongchars, wrongpos, correctpos)
      print(bestword)
  
   answer = input("Did you get it right? ")
   if answer.lower() == 'yes':
      break
   badchars = input("Which letters weren't correct? ")
   for char in badchars:
      if char.upper() in letters and char.lower() in bestword and char.lower() not in wrongchars:
         del lettercount[char.lower()]
         wrongchars.append(char.lower())
         
   poschars = input("Which letters were in the wrong position? ")
   for char in poschars:
      if char.lower() not in correctchars:
         correctchars.append(char.lower())
      if char.upper() in letters and char.lower() in bestword.lower():
         wrongpos[char.lower()].append(bestword.lower().find(char.lower()))
   cposchars = input("Which letters were in the correct position? ")
   for char in cposchars:
      if char.lower() not in correctchars and char.lower() not in wrongchars:
         correctchars.append(char.lower())
      if char.upper() in letters and char.lower() in bestword.lower() and char.lower() not in correctpos:
         correctpos[char.lower()] = bestword.lower().find(char.lower())
      
   bestword = ""
   bestscore = 0
   correctcount = 0

   print(bestword)
