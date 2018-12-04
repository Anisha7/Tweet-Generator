# sample word from state histogram
from learnMarkov import Markogram
import random

# takes in a Markov Chain histogram of words from file
# returns a random word
def getRandomWord(histogram):
    index = random.randint(0, len(histogram.keys()) - 1)
    print(histogram.keys())
    return (histogram.keys())[0][index]

# takes in a histogram and length of the sentence
def makeSentence(histogram, n):
    if (n == 0):
        return ''
    
    prev = getRandomWord(histogram)
    result = '' + prev
    for i in range(n-1):
        result += ' '
        # get word that is 'allowed' after prev word
        options = histogram[prev]
        found = False
        index = random.randint(0, len(options)-1)
        # find valid word
        while (found == False):
            if (options[index][1] > 0):
                found = True
            else: 
                index = random.randint(0, len(options)-1)
        
        result += ' ' + options[index][0]
        histogram[prev][index] = (options[index][0], options[index][1] - 1)
        
        # change prev to newly added word, to find next valid word
        prev = options[index][0]

    result += '.'
    return result

if __name__ == '__main__':
    path = "prideandprejudice.txt"
    with open(path) as file:
        content = (file.read()).split()
    histogram = Markogram(content)
    print(makeSentence(histogram, 5))
    