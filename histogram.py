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

# use sets?
# use dictionaries?

def inDict(word, d):
    if d.get(word) == None:
        return False
    return True

    #return (word in d)

# returns a dictionary with key: word, value: number of occurances
def histogram() :
    words_dict = dict()
    file = open('prideandprejudice.txt','r')
    content = (file.read()).split()
    for i in range(len(content)):
        if inDict(content[i], words_dict):
            words_dict[content[i]] = 1 + words_dict[content[i]]
        else : 
            words_dict[content[i]] = 1
   
    return words_dict


def unique_words(words_dict) :
    return len(words_dict.keys())

def frequency(words_dict, word):
    if word in words_dict:
        return words_dict[word]
    return 0

def game() :
    #content
    words_dict = histogram()
    #game
    print("What would you like to know?")
    print("(A) How many unique words are in Pride and Prejudice?")
    print("(B) How many times does a word occur?")
    option = input("Choose A or B: ")

    if (option == 'A' or option == 'a'):
        print(unique_words(words_dict))
    elif (option == 'B' or option == 'b'):
        word = input("Which word? ")
        print(frequency(words_dict, word))
    else :
        print("That's not valid")
        return game()

def run() :
    gameState = input("Do you want to play (y/n)? ")
    while (gameState == 'y' or gameState == 'Y'):
        game()
        gameState = input("Do you want to play again (y/n)? ")

run()