# build a script that randomly rearranges a set of words provided as command-line arguments to the script.
import sys
import random


# shuffles given list of words
def rearrange(args):
    result = []
    while (len(args) > 0) :
        i = random.randint(0, len(args)-1)
        result.append(args.pop(i))
    
    return result

# takes string word and reverses it
def reverse_word(word):
    rev_word = ""
    for i in range(len(word)):
        rev_word += word[len(word) - 1 - i]
    
    return rev_word


# takes in a string sentence and returns reversed string
def reverse_sentence(sentence):
    l = sentence.split(" ")
    new = ""
    for i in range(len(l)):
        new += l[len(l) - 1 - i] + " "
    return new;


def game():
    option = input("Do you want to (A) rearrange, (B) reverse word, (C) reverse sentence? ")
    if (option == 'A' or option == 'a'):
        args = input("Give me a list of words: ")
        result = rearrange(args.split(" "))
        print(" ".join(result))
    elif (option == 'B' or option == 'b'):
        word = input("Give me a word to reverse: ")
        result = reverse_word(word)
        print(result)
    else :
        sentence = input("Give me a sentence to reverse: ")
        result = reverse_sentence(sentence)
        print(result)
    return;

def run():
    
    # args = sys.argv[1:]
    # result = rearrange(args)

    # print(" ".join(result))

    gameState = input("Do you want to play (y/n)? ")
    while (gameState == 'y' or gameState == 'Y'):
        game();
        gameState = input("Do you want to play again (y/n)? ")
    
    return;

run()