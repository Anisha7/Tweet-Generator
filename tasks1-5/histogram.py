''' In this tutorial, we'll be writing a program which, given a source body of text, can perform operations to answer questions such as:

What is the least/most frequent word(s)?
How many different words are used?
What is the average (mean/median/mode) frequency of words in the text?''' 

''' A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, 
your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears 
in the source text.
A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. For 
example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. 
For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.'''

# cheat way to do it: 
    # import collections
    # collections.counter(opened file split by ' ') return a dictionary
    # .items() converts that to a tuple

# checks if word is in dictionary
def inDict(word, d):
    if d.get(word) == None:
        return False
    return True

# returns a dictionary with key: word, value: number of occurances
# note: check for punctuation 'of?'
def histogram() :
    words_dict = dict()
    with open('prideandprejudice.txt') as file:
        # initialize file as a list of words
        content = (file.read()).split()

    for i in range(len(content)):
        # if word is in dictionary, increment count
        if inDict(content[i], words_dict):
            words_dict[content[i]] = 1 + words_dict[content[i]]
        # else, add word to dictionary
        else : 
            words_dict[content[i]] = 1
   
    return words_dict

# returns the number of unique words in the file
def unique_words(words_dict) :
    return len(words_dict.keys())

# returns how many times a word occurs in the file
def frequency(words_dict, word):
    if word in words_dict:
        return words_dict[word]
    return 0

# creates the game loop
def game() :
    # initialize the histogram
    words_dict = histogram()
    
    # print game instructions
    print("What would you like to know?")
    print("(A) How many unique words are in Pride and Prejudice?")
    print("(B) How many times does a word occur?")
    option = input("Choose A or B: ")

    # evaluate input from user and give appropriate action
    if (option == 'A' or option == 'a'):
        print(unique_words(words_dict))
    elif (option == 'B' or option == 'b'):
        word = input("Which word? ")
        print(frequency(words_dict, word))
    else :
        print("That's not valid")
        # loop again if invalid input
        return game()

# run the game
def run() :
    gameState = input("Do you want to play (y/n)? ")
    while (gameState == 'y' or gameState == 'Y'):
        game()
        gameState = input("Do you want to play again (y/n)? ")

if __name__ == '__main__' :
    run(); 