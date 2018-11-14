# Learn a Markov chain from a corpus. You've already written code to 
# find how often a token appears in a corpus, but now you need to 
# find how often a token appears after another token.

# Ideas
## dictionary - key : word; value : [(word, count), (word, count)] that occur after the word

#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility

class Markogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # self.d = Counter()
        # Count words in given list, if any
        if word_list is not None:
            prev = ''
            for word in word_list:
                self.add_count(word, prev)
                prev = word

    # increments count for word in histogram
    def add_count(self, word, prev, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if (prev != ''):
            if (self.get(prev) != None):
                # add word to prev or increment its count
                data = self[prev]
                index = -1
                for i in range(len(data)):
                    if (data[i][0] == word):
                        index = i
                        break
                # if word is already there, increment its count
                if (index > -1) :
                    newTup = (word, data[index][1] + 1)
                    self[prev].remove(data[index])
                    self[prev].append(newTup)
                # else add word with count 1
                else:
                    self[prev].append((word,1))
               
            else:
                # add to dictionary
                self[prev] = [(word, 1)]
                
        self.tokens += count
        self.types += 1
        
    # returns how many times a word occured
    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        count = 0
        if (self.__contains__(word)):
             for key in self.keys():
                 data = self[key]
                 for i in range(len(data)):
                     if (data[i][0] == word):
                         count += data[i][1]
        return count

    # replace inbuilt contains function
    # checks if a word is in the histogram/dictionary
    def __contains__(self, word):
        if self.get(word) != None:
            return True
        return False

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Markogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
