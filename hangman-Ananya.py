
# coding: utf-8

# In[33]:

import random
secretWords = {'passport':'An official Document', 'hangman':'The name of the game', 'yellow':'A color', 'clock':'time measuring machine', 'absinthe':'75% ABV alcohol', 'dictionary':'book of words', 'arsenic':'Atomin weight 75'}

def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    blank = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
            
        
def hangman(secretWords):
    secretWord = random.choice(list(secretWords.keys()))
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False
    
    print ('HANGMAN')
    print (('The word is ') + intro + (' letters long.'))
    print ('Hint :'+ secretWords[secretWord])

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ( str(mistakesMade) + (' guesses left.'))
        guess = input('\nPlease guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print (("already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))

            else:
                lettersGuessed.append(guess)
                print (('Correct: ') + getGuessedWord(secretWord, lettersGuessed))
        else:
            if guess in lettersGuessed:
                print (("already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print (('Wrong: ') + getGuessedWord(secretWord, lettersGuessed))

    if wordGuessed == True:
        print ('\nYOU WON!')
    elif mistakesMade == 0:
        print (('No more guesses left. The word was:\n') + secretWord)

answer = 'y'
while answer=='y':
    hangman(secretWords)
    answer = input("\nDo you want to continoue?: y or n \n")

print("\nThank you")
    


# In[25]:

dict1 = {'book':'nancy drew', 'house':'1602'}
for i,j in  enumerate(dict1):
    print(j)
    


# In[23]:

dict1['book']


# In[28]:

list(dict1.keys())


# In[ ]:



