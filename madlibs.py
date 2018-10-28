# print sentences with a blank
# take input to complete sentence
# return that
# play again
import random

def getRandomSentence() :
    file = open('cwh.txt','r')
    found = False
    word = ""
    content = (file.read()).split("<>")
    while (found == False):
        i = random.randint(0,len(content)-1)
        word = content[i]
        if '__________' in word:
            found = True
    return word

def run():
    gameState = 'Y';
    gameState = input("Do you want to play? (Y/N) : ")
    while (gameState == 'Y' or gameState == 'y') :
        sentence= getRandomSentence()
        print(sentence)
        word = input("fill in the blank: ")
        sentence = sentence.replace('__________', word)
        print(sentence)
        gameState = input("Do you want to play again? (Y/N) : ")

run()