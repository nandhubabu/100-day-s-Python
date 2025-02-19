import random

rand = random.randint(0,2)

choise = input('What do you chose ? 0 for Rock, 1 for Paper and 2 for Scissors ?')
if choise == '0':
    print('you chosed rock')
    if rand == 0:
        print('computer chosed rock')
        print('Draw')
    elif rand == 1:
        print('computer chosed paper')
        print('You lose')
    elif rand == 2:
        print('computer chosed scissors')
        print('You win')
elif choise == '1':
    print('you chosed paper')
    if rand == 0:
        print('computer chosed rock')
        print('You win')
    elif rand == 1:
        print('computer choise')
        print('Draw')
    elif rand == 2:
        print('computer chosed scissors')
elif choise == '2':
    print('you chosed scissors')
    if rand == 0:
        print('computer chosed rock')
        print('You lose')
    elif rand == 1:
        print('computer chosed paper')
        print('You win')
    elif rand == 2:
        print('computer chosed scissors')
        print('Draw')
else:
    print('Invalid number')