# use a queue to set up a markov chain with before and curr words 
# making a 2nd order markov chain

# ideas
    # use linked lists?
from linkedlist import LinkedList
from Queue import Queue
from dictogram import Dictogram

# takes in a string corpus and converts it to a 2nd order markov chain
class MarkovChain(Dictogram) :

    def __init__(self, items=None, n = 2):
        super(MarkovChain, self).__init__()
        # key: (I, went) -> value {dict} ({(went, left):2/3, (went,right):1/3})
        self.order = n
        self.items = items
        self.append()

    def find(self, curr):
        # takes curr and finds dict key (prev,curr)
        for key in self.keys():
            if key[1] == curr:
                return key
        return None

    # use queue to get a tuple
    def get_tuple(self, index):
        temp_queue = Queue()

        # init queue
        n = self.order
        
        while (n != 0) :
            if (index >= len(self.items)):
                break
            temp_queue.enqueue(self.items[index])
            index += 1
            n -= 1
        

        result_list = []
        # queue to tuple
        while (temp_queue.isEmpty() == False):
            result_list.append(temp_queue.dequeue())
        #print(tuple(result_list))
        return tuple(result_list)

        
    def append(self):

        # add first word into dict
        # self[('', self.items[0])] = Dictogram()

        for i in range(0, len(self.items)-1):
            # make a tuple (prev, curr) => queue?
            # key = (word_list[i], word_list[i+1])
            key = self.get_tuple(i)
            # add tuple as the dict value to the key that has 'prev' as its tuple[1] element
            prev_key = self.find(self.items[i])
            if prev_key != None:
                # check its values
                d = self[prev_key]
                result = d.get(key)
                # if our key exists in values
                if (result != None):
                    # increment count
                    # self[prev_key][value] += 1
                    self[prev_key].add_count(key)
                # else
                else:
                    # add it with count 1
                    # self[prev_key][value] = 1
                    self[prev_key].add_count(key, 1)

            # add our key as a key pointing to an empty dict
            self[key] = Dictogram()

    def printMarkov(self):
        for key in self.keys():
            print(key, ': ', self[key])
            
        return