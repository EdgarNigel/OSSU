# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
	guessed = True
	for i in range(len(secretWord)):
		if secretWord[i] in lettersGuessed:
			guessed = guessed and True
		else:
			return False
	
	return guessed



def getGuessedWord(secretWord, lettersGuessed):
	guessed = []
	
	for i in range(len(secretWord)):
		if secretWord[i] in lettersGuessed:
			guessed.append(secretWord[i])
		else:
			guessed.append("_")
	
	return " ".join(guessed)



def getAvailableLetters(lettersGuessed):
	abc = string.ascii_lowercase
	notguessed = []
	
	for i in range(len(abc)):
		if abc[i] not in lettersGuessed:
			notguessed.append(abc[i])
	
	return "".join(notguessed)
    

def hangman(secretWord):

	print("Welcome to the game, Hangman!")
	print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

	lettersGuessed = []
	mistakesMade = 0
	
	while mistakesMade < 8 and not isWordGuessed(secretWord, lettersGuessed):
		print("------------")
		print("You have " + str(8-mistakesMade) + " guesses left.")
		print("Available letters: " + getAvailableLetters(lettersGuessed))
		guess = raw_input("Please guess a letter: ").lower()
		
		if guess in lettersGuessed:
			print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
		else:
			lettersGuessed.append(guess)
			if guess in secretWord:
				print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
			else:
				print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
				mistakesMade += 1
	
	if isWordGuessed(secretWord, lettersGuessed):
		print("------------")
		print("Congratulations, you won!")
	else:
		print("------------")
		print("Sorry, you ran out of guesses. The word was " + secretWord + " .")
	
	
		



		



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

