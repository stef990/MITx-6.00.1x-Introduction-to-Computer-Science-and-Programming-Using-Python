def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for x in secretWord:
        if (x in lettersGuessed) == False:
            return False
            break
    return True
        
        
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for x in secretWord:
        if (x in lettersGuessed) == False:
            word += ' _ '
        else:
            word += x
    return word 
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    word = ''
    import string
    for x in string.ascii_lowercase:
        if (x in lettersGuessed) == False:
            word += x
    return word
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    print('-----------')
    guesses = 8
    lettersGuessed =''
    while (guesses >0 and not(isWordGuessed(secretWord, lettersGuessed))):

        print('You have ' + str(guesses) + ' guesses left')
        print('Available letters:' + str(getAvailableLetters(lettersGuessed) ))
        userinput = str(raw_input('Please guess a letter:'))

        if (userinput in lettersGuessed):
            print('Oops! You\'ve already guessed that letter:' + str(getGuessedWord(secretWord,lettersGuessed)))
        elif (userinput in secretWord):
            lettersGuessed += userinput.lower()
            print('Good guess: ' + str(getGuessedWord(secretWord,lettersGuessed)))
        elif (userinput in lettersGuessed):
            print('Oops! You\'ve already guessed that letter:' + str(getGuessedWord(secretWord,lettersGuessed)))
        else:
            print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord,lettersGuessed)))
            guesses -=1
        lettersGuessed += userinput.lower()
        print('-----------')
    if isWordGuessed(secretWord, lettersGuessed)==False:
        return "Sorry, you ran out of guesses. The word was " + secretWord
    else:
        return "Congratulations, you won!"
    
    
