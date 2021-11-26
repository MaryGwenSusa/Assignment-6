import random
def header():
    title = "**Addition Practice Quiz**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def determineAns():
    answer = digit1 + digit2 
    equation = int(input ("What is %s + %s? \033[94m" % (digit1, digit2)))
    if answer == equation:
        print("\033[00m\33[95mYou are doing great! I am proud of you <<<333\33[00m")
        return True
    else:
        print("\033[92mPlease, try again! ^_^\033[00m")

header()
quizScore = 0 # first initialization (for creating variables with changing values)
number = 1 # second initialization
"""These are variables created for changeable value
"""

digit1 = random.randint(0,99)
digit2 = random.randint(0,99)
print(f"Question #" + str(number)) 
correct = determineAns()
if correct == True:
    quizScore +=1


print(f"\033[33mYour final score is {quizScore}/10. Do {quizScore} claps for yourself today.\033[00m")

