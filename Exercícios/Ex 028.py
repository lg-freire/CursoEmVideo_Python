import random
from time import sleep
num = int(random.randrange(0, 5))
inp = int(input('GUESS A NUMBER FROM 0 TO 5 OR I WILL EAT YOUR SOUL! '))
sleep(3)
print('Good job, bro.' if inp == num else 'DIE, YOU WORTHLESS MEATBAG!!!!')
