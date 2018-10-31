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

# return true if a is before b
# return false if a is after b
def word_order(a,b):
    order = [a,b]
    order.sort()

    if (order[0] == a):
        return True
    return False

'''
def find_by_mid(word, l, i):
    # not found/out of bounds
    if (i >= len(l)) :
        return -1
    if (i == -1):
        return -1
    # found
    if (l[i][0] == word):
        return i
    elif (i == 0):
        return -1
    
    # check cases: if word comes before or after curr list item
    if word_order(word[0], l[i][0]):
        #(l[i][0][0] > word[0])
        if (i/2 < 1):
            return find_by_mid(word, l, 0)
        return find_by_mid(word, l, int(i/2))
    else:
        return find_by_mid(word, l, i*2 -1)
'''

# get index for where the word is in list l
# assume list is sorted alphabetically
# return -1 if not found
def find(word, l):
    
    for i in range(len(l)):
        if (l[i][0] == word):
            return i
    return -1


# add to list in sorted order
def add(word, l):
    for i in range(len(l)):
        if (word_order(word, l[i][0])):
            l.insert(i, [word, 1])
            return l
    l.append([word, 1])
    return l
    
# returns a list with lists: [word, value(number of occurances)]
def histogram():
    words_list = []
    with open('prideandprejudice.txt') as file:
        content = (file.read()).split()
    for i in range(len(content)):
        index = find(content[i], words_list)
        if index != -1:
            # words_list[content[i]] = 1 + words_dict[content[i]]
            # increment count for that word
            words_list[index][1] += 1
        else : 
            # add function to add in sorted order instead of appending and sorting
            # words_list.append([content[i],1])
            # sortList(words_list)
            words_list = add(content[i], words_list)
   
    return words_list


def unique_words(l):
    return len(l)

def frequency(l, word):
    index = find(word, l)
    if index != -1:
        return l[index][1]
    return 0

def game(words_list) :
    
    #game
    print("What would you like to know?")
    print("(A) How many unique words are in Pride and Prejudice?")
    print("(B) How many times does a word occur?")
    option = input("Choose A or B: ")

    if (option == 'A' or option == 'a'):
        print(unique_words(words_list))
    elif (option == 'B' or option == 'b'):
        word = input("Which word? ")
        print(frequency(words_list, word))
    else :
        print("That's not valid")
        return game()

def run() :
    #content
    words_list = histogram()
    gameState = input("Do you want to play (y/n)? ")
    while (gameState == 'y' or gameState == 'Y'):
        game(words_list)
        gameState = input("Do you want to play again (y/n)? ")

run()