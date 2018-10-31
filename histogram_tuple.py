# [(word, count), (word, count)]

# return true if a is before b
# return false if a is after b
def word_order(a,b):
    order = [a,b]
    order.sort()

    if (order[0] == a):
        return True
    return False


# add to list in sorted order
def add(word, l, n):
    for i in range(len(l)):
        if (word_order(word, l[i][0])):
            l.insert(i, (word, n))
            return l
    l.append((word, n))
    return l

# get index for where the word is in list l
# assume list is sorted alphabetically
# return -1 if not found
def find(word, l):
    
    for i in range(len(l)):
        if (l[i][0] == word):
            return i
    return -1
    
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
            new_tup = (words_list[index][0], 1 + words_list[index][1])
            del words_list[index]
            words_list = add(new_tup[0], words_list, new_tup[1])
            del new_tup

            
        else : 
            # add function to add in sorted order instead of appending and sorting
            # words_list.append([content[i],1])
            # sortList(words_list)
            words_list = add(content[i], words_list, 1)
   
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
        return game(words_list)

def run() :
    #content
    words_list = histogram()
    gameState = input("Do you want to play (y/n)? ")
    while (gameState == 'y' or gameState == 'Y'):
        game(words_list)
        gameState = input("Do you want to play again (y/n)? ")

run()