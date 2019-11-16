import string

def isWordGuessed(secretWord, guessed):
    for indx in guessed:
        if guessed==secretWord:
            guess = True
            break       
        elif indx in secretWord:
            guess = True
            print('Correct! ',guessed,'is included in the mystery word!')
        else:
            print("Wrong!")
            guess = False
                    
    return guess

def getGuessedWord(secretWord, lettersGuessed):
    guessedlist = list(lettersGuessed)
    guessedWord = ''
    
    for indx2 in secretWord:
        if lettersGuessed==secretWord:
            guessedWord = lettersGuessed
            break
        elif indx2 in guessedlist:
            guessedWord = guessedWord + indx2
        else:guessedWord = guessedWord + '_'
    
    return guessedWord


def getAvailableletters(lettersGuessed):
    l = list(string.ascii_lowercase)
    availletters = ''
    
    for indx3 in l:
        if indx3 not in lettersGuessed:availletters+=indx3
    
    return availletters

def Hangaroo(secretWord):

    tries = 8
    lettersGuessed = []
    availletters = string.ascii_lowercase
    guessedWord = ''
    
    print("Let's play Hangaroo!")
    while tries>0:

        casesensitive_guessed = input("Enter a letter(press 0 to quit) ") 
        guessed = casesensitive_guessed.lower()
        
        if guessed =='0':break
        
        if guessed in lettersGuessed:
            print('You have already entered that letter')
            print(guessedWord)
            continue
        
        lettersGuessed.append(guessed)
        
        availletters = getAvailableletters(lettersGuessed)

        rightletter = isWordGuessed(secretWord,guessed)            
        if rightletter == False: 
            tries -= 1
            if tries ==0: 
                print("Oh no! You did not guess the right word. The correct word is ",secretWord)
                break
            print("You only have",tries," tries left.")
            
        guessedWord = getGuessedWord(secretWord,lettersGuessed)
        print(guessedWord) 


        if guessedWord == secretWord:
            print("Correct! You have guessed the right word.") 
            break
    
    return
            
        
    
                    
                
                    
                
            

