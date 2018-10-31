
# take a word
# rearrange it and check if in dictionary
# return new word

import random
def validWord(word, d):
    return word in d

def rearrange(args):
    result = []
    while (len(args) > 0) :
        i = random.randint(0, len(args)-1)
        result.append(args.pop(i))
    
    return result

# does not work properly
# do manually instead of random
def makeAnagram(word):
    char_list = []
    for i in range(len(word)):
        char_list.append(word[i])

    new_list = rearrange(char_list)

    new_word = ''.join(new_list)
    return new_word 



def run():
    file = open('/usr/share/dict/words','r')
    content = list(file)

    gameState = input('Do you want to play? (y/n): ')
    while (gameState == 'Y' or gameState == 'y'):
        word = input('What word should I make an anagram for?')
        valid = False
        count = 0

        while(valid == False and count < 10):
            new_word = makeAnagram(word)
            valid = validWord(word, content)
            count += 1

        if (valid == False) :
            print("no anagram found")
        else: print(new_word)
        gameState = input('Do you want to play again? (y/n): ')

    return


run()