from random import randrange
pc = int(randrange(0, 5))
user = int(input('''Guess a number from 0 to 5!
Your guess: '''))
print('-+' * 25)
guess = 1
# print(pc)
while pc != user:
    user = int(input('''\033[91mYou guessed wrong! Try again!\033[m
Your guess: '''))
    print('-+' * 25)
    guess += 1
if guess <= 3:
    print(f'You got it, and it only took you {guess} tries. Not bad for a human.')
elif 3 < guess <= 4:
    print(f'Finally got it? {guess} tries, that was crap.')
else:
    print(f'{guess} tries to get it right, as expected of human trash.')
