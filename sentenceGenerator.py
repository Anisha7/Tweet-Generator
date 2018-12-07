from markovchain2 import MarkovChain

# open hamlet
# list() convert
# pass it into dictogram
# make sentence with it

def file_to_list():
    path = "hamlet.txt"
    with open(path) as file:
        content = (file.read()).split()
    
    histogram = MarkovChain(content)
    histogram.printMarkov()

if __name__ == '__main__':
    file_to_list()