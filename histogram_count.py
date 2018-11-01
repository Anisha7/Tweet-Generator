
# unique words

# word to add to list l at count n
def add(word, l, n, i):
    print("adding")
    # if its a new word
    print(l)
    if (len(l) == 0): 
        l.append((n, [word]))
    elif (n == 1 & len(l) > 0):
        if (l[i][1] != None):  
            add_word = l[i][1].append(word)
        else:
            add_word = [].append(word)
        #del l[i]
        l.pop(i)
        l.insert(i, (1, add_word))   
    # if word exists
    else:
        if (i < len(l)):
            # remove from old tuple
            new_list = l[i][1].remove(word)
            #del l[i]
            l.pop(i)
            l.insert(i, (n, new_list))
            print(new_list)
            print(i)

        if (i + 1 < len(l)):
            # add to next tuple
            add_word = l[i+1][1].append(word)
            #del l[i+1]
            l.pop(i+1)
            l.insert(i+1, (n+1, add_word))   
            
        else:
            l.append((n+1, [word]))

    return l

# find a word, return index where its at
def find(word, l):
    for i in range(len(l)):
        word_list = l[i][1]
        if word_list != None:
            for j in range(len(word_list)):
                if word == word_list[j]:
                    return i
    return -1

def unique_words(l):
    words = 0
    for i in range(len(l)):
        words += len(l[i][1])
    return words

def frequency(l, word):
    index = find(word, l)
    return l[index][0]

# implement words list with counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]
def histogram() :
    words_list = []
    with open('prideandprejudice.txt') as file:
        content = (file.read()).split()
    
    for i in range(len(content)):
        index = find(content[i], words_list)
        if (index != -1) :
            # pop and add to next tuple
            add(content[i], words_list, words_list[index][0], index)
        else :
            # add to first count
            add(content[i], words_list, 1, 0)

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