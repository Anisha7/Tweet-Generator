

import sys
import random
import os

# counts total words (NOT UNIQUE)
def countWords(hist):
    # tot count
    totCount = 0
    for k in hist.keys():
        totCount += hist[k]
    return totCount

# randomly returns a word taking probability in consideration
def randomArg(hist):
    # tot count
    totCount = countWords(hist)
    
    
    random_num = random.randint(0, totCount-1)

    for k in hist.keys():
        random_num -= hist[k]
        if (random_num < 0):
            return k

    # should never get here
    return hist.keys()[0]


# returns a dictionary with key: word, value: number of occurances
# note: check for punctuation 'of?'
def histogram(content) :
    words_dict = dict()
    
    for i in range(len(content)):
        if inDict(content[i], words_dict):
            words_dict[content[i]] = 1 + words_dict[content[i]]
        else : 
            words_dict[content[i]] = 1
   
    return words_dict

# returns true if path is a file
def isFile(path):
    return os.path.isfile(path)

# read file if it is a file 
# convert it to a dictionary histogram
def readFile(path, args):
    if (isFile(path)):
        # read file
        # put its contents in args
        with open(path) as file:
            content = (file.read()).split()
        args = content
    return histogram(args)

# checks if word is in dictionary
def inDict(word, d):
    if d.get(word) == None:
        return False
    return True

# samples it n times and returns a dictionary of how many times each word occurs
def sample(args, n):
    d = dict()
    while(n > 0):
        word = randomArg(args)
        if (inDict(word, d)):
            d[word] = d[word] + 1;
        else:
            d[word] = 1
        
        n -= 1
    return d

def probability(d, key, n):
    # gives probability for each word
    prob = d[key]/n
    return round(prob, 3)

def printProbabilities(d, n):
    for k in d.keys():
        result = k + ": "
        prob = probability(d, k, n)
        result += str(prob)
        print(result)

def printDict(d):
    for k in d.keys():
        result = k + ": " + str(d[k])
        print(result)

def expectedProbabilities(hist):
    totCount = countWords(hist)
    expectedProb = dict()
    for k in hist.keys():
        prob = round(hist[k]/totCount, 2)
        expectedProb[k] = prob
    
    return expectedProb

def printExpected(expectedProb):

    for k in expectedProb.keys():
        result = k + ": " + str(expectedProb[k])
        print(result)
    return

def run():
    args = sys.argv[1:]
    path = args[0]

    args = readFile(path, args)
    #print(randomArg(args))
    n = 100000
    d = sample(args, n)

    print("Expected:")
    printExpected(expectedProbabilities(args))

    print("Probabilities: ")
    printProbabilities(d, n)
    print("occurances for " + str(n) + " cases: ")
    printDict(d)


run()


