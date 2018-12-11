from markovchain2 import MarkovChain
import random
# open hamlet
# list() convert
# pass it into dictogram
# make sentence with it

def file_to_markov():
    path = "hamlet.txt"
    with open(path) as file:
        content = (file.read()).split()
    
    markov = MarkovChain(content)
    # markov.printMarkov()

    return markov
# first letter capital
def findFirst(markov):
    found = False
    while (found == False):
        key = random.choice(list(markov.keys()))
        if (key[0].istitle()):
            return key
    return

def random_sentence(markov):
    #key = findFirst(markov)
    sentence = ''
    key = random.choice(list(markov.keys()))
    for i in range(len(key)):
        sentence += key[i] + ' '
    
    next_exists = True
    options = markov[key]
    while (next_exists):
        if (len(options.keys()) > 0):
            next_key = random.choice(list(options.keys()))
            # take count in account
            count = options[next_key]
            if count > 0:
                sentence += next_key[len(next_key)-1] + ' '
                options[next_key] -= 1
            # dont take count in account
            # current because small corpus
            # change later
            else: 
                sentence += next_key[len(next_key)-1] + ' '
            
            options = markov[next_key]
        else:
            next_exists = False
    
    return sentence.strip()

def make_quote(markov):
    paragraph = ''
    for i in range(10):
        sentence = random_sentence(markov)
        paragraph += sentence + ' '
    return paragraph

def run(markov):
    game = True
    while (game):
        para = make_quote(markov)
        print(para)
        loop = input("Want another sentence? (y/n)")
        if (loop == 'n' or loop != 'y'):
            game = False
    return

if __name__ == '__main__':
    markov = file_to_markov()
    run(markov)
    

    


