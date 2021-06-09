import random
while True:
    election = input('Do you want to play a game with me? Y/N: ').lower()
    if election == 'y':
        print('so, try to guess my number from 1 to 100...')
        break
    elif election == 'n':
        print('sorry, could you repeat that?')
    else:
        print('try again')
secretNumber = random.randrange(1, 100)
score = 100
print('your score is: ', score, end = '')
guess = int(input(' , so make a guess: '))
clues = [[],[],False]
for i in range(5):
    clues[0].append(secretNumber * (i + 2))
for i in range(2, secretNumber):
    if (secretNumber % i) == 0:
        clues[1].append(i)
clues[2] = (len(clues[1]) == 0)

def giveAClue(guessF):
    while True:
        option = random.randrange(0,3)
        if option == 0:
            if len(clues[0]) > 0:
                multiple = clues[0].pop(random.randrange(0, len(clues[0])))
                print('I´ll give you a clue:', multiple, 'is a multiple of the secret number')
                break
            else:
                continue
        elif option == 1:
            if clues[2]:
                print("listen: the secret number is a prime")
                clues[2] = False
                break
            else:
                if len(clues[1]) > 0:
                    divisible = clues[1].pop(random.randrange(0, len(clues[1])))
                    print('I´ll give you a clue: the secret number is divisible by', divisible)
                    break
                else:
                    continue
        else:
            if guessF > secretNumber:
                print('I´ll give you a clue: that was too big, try some different')
                break
            else:
                print('I´ll give you a clue: that number is smaller than the secret number')
                break

while guess != secretNumber:
    giveAClue(guess)
    score -= 1
    guess = int(input('make another guess: '))
print('very good, you did it and your score was: ',score)
