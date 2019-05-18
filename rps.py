import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def random_play():
    """vybírá náhodně ze tří možností r, p, s"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'rock' and computer == 'paper' or human == 'scissors' and computer == 'rock' or human == 'paper' and computer == 'scissors':
        return 'computer'
    else:
        return 'human'

def main(input=input):

    human = None

    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')

    computer = random_play()
    print(computer)
    print(determine_game_result(human, computer))

if __name__ == '__main__':
    main()
