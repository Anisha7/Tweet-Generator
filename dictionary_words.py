# use words from file: /usr/share/dict/words
# Take 1 argument: amount of words to select
# put the words together in a 'sentence' (order doesn't matter, it doesn't have to make sense)
import sys;
import random;

words = int(sys.argv[1]);
file = open('/usr/share/dict/words','r');
content = list(file);

result = "";
while (words > 0) :
    index = random.randint(0, len(content) - 1);
    result += content[index].strip() + " ";
    words -= 1;

print(result);