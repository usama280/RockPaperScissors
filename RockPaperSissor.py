import random


def play():
    user = input('Rock, paper, or scissor (r,p,s): ')
    comp = random.choice(['r','p','s'])

    print(f'Your choice: {user} \nComp choice: {comp}')

    if (user == comp):
        return 'tie'
    elif is_win(user, comp):
        return 'win'
    return 'lose'


def is_win(u,c):
    if (u == 'r' and c == 's') or (u == 's' and c == 'p') or (u == 's' and c == 'p'):
        return True

print(play())