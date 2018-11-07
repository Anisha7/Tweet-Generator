import sys
import random

# content is a list of words
# words is the number of random words to return
# returns a string of words divided by spaces
def random_dictionary_word(content, words) :
    # gets a random number between 0 & length of dictionary
    # and adds word at that index to result string with a space at the end
    result = ""
    while (words > 0) :
        index = random.randint(0, len(content) - 1)
        result += content[index].strip() + " "
        words -= 1

    # once we have the number of words asked for:
    # print(result)
    return result

if __name__ == "__main__":
     # gets the number of words we need
    words = int(sys.argv[1])
    # opens & closes our dictionary and converts it to a list
    with open('/usr/share/dict/words','r') as file:
        content = list(file)
    
    print(random_dictionary_word(content, words));