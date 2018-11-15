# sample word from state histogram
from learnMarkov import Markogram
import random

# takes in a Markov Chain histogram of words from file
# returns a random word
def getRandomWord(histogram):
    index = random.randint(0, len(histogram.keys()) - 1)
    return (histogram.keys())[index]

if __name__ == '__main__':
    path = "prideandprejudice.txt"
    with open(path) as file:
        content = (file.read()).split()
    histogram = Markogram(content)
    print(getRandomWord(histogram))
    