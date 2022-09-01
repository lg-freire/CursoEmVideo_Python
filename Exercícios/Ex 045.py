import random
play = str.lower(input('Play me! Rock, paper, scissors!\nYour move: ').strip())
cpu = random.randrange(1, 4)
if play == 'rock':
    play = 1
elif play == 'paper':
    play = 2
elif play == 'scissors':
    play = 3
if play == cpu:
    print("It's a draw.")
elif play == 1 and cpu == 2 or play == 2 and cpu == 3 or play == 3 and cpu == 1:
    print('I win, bitch!')
elif play == 1 and cpu == 3 or play == 2 and cpu == 1 or play == 3 and cpu == 1:
    print('I accept defeat.')
else:
    print("Just say rock, paper or scissors, dumbass.")
