#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
                    
    def word_order(self, a,b):
        order = [a,b]
        order.sort()

        if (order[0] == a):
            return True
        return False

    def find(self, word):
        
        for i in range(len(self)):
            if (self[i][0] == word):
                return i
        return -1

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increase word frequency by count
        index = self._index(word)
        # increment if found
        if index != -1:
            self[index] = (word, self[index][1] + count)
        # add as a new item if not found
        else:
            self.types += 1
            self.append((word, count))
            
        self.tokens += count


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        index = self._index(word)
        if (index < 0):
            return 0
        return self[index][1]

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        if (self._index(word) == -1):
            return False
        return True

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        for i in range(len(self)):
            if (self[i][0] == target):
                return i
        return -1

    # def __eq__(self, other):
    #     if (self.types != len(other)):
    #         return False
    #     for i in range(len(other)):
    #         if (self.__contains__(other[i]) == False):
    #             return False
    #     print('here')
    #     return True

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
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
