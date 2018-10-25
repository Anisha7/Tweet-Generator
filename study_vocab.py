# vocab study game
# give a word, get definition input, output real definition
import random;



def str_equal(s1, s2) :
    s1 = s1.strip().split(" ");
    s2 = s2.strip().split(" ");

    if (len(s1) != len(s2)) :
        return false;
    
    for i in range(0, len(s1)) :
        if (s1[i] != s2[i]) :
            return false;

    return true;


def play(score) :
    file = open('words.txt','r');
    content = list(file);

    index = random.randint(0, len(content));
    line_list = content[index].split(" ");
    result = line_list[0];

    definition = input("What's the definition of " + result + "?");
    answer = "";
    for i in range(2, len(line_list)):
        answer += line_list[i] + " ";

    if (str_equal(definition, answer)): 
        print("You were correct");
        score += 1;
    else:
        print("The correct definition is: " + answer + "");

    return score;
    
def run() :
    gameState = input("Do you want to play? (Y/N): ");
    score = 0;
    while (gameState == "Y") :
        score = play(score);
        print("Your Score: " + str(score));
        gameState = input("Do you want to play again? (Y/N): ");

run();
