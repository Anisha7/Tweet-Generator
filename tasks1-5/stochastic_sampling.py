import sys
import random
import os

# returns true if path is a file
def isFile(path):
    return os.path.isfile(path)

# read file if it is a file 
# convert it to a list of words
def readFile(path, args):
    if (isFile(path)):
        # read file
        # put its contents in args
        with open(path) as file:
            content = (file.read()).split()
        args = content
    
    return args

# get random word from list of words (args)
def randomArg(args):
    n = random.randint(0, len(args)-1)
    return args[n]

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

def run():
    args = sys.argv[1:]
    path = args[0]

    args = readFile(path, args)
    #print(randomArg(args))
    n = 100000
    d = sample(args, n)
    print("Probabilities: ")
    printProbabilities(d, n)
    print("occurances for " + str(n) + " cases: ")
    printDict(d)


run()

