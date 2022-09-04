import sys
from random import randint
from time import sleep
l = ('Rock', 'Paper', 'Scissors')
pcplay = randint(0, 2)
print("""PICK YOUR POISON:
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissors""")
uplay = int(input('Play: '))
if uplay >= 3:
    print('INVALID INPUT!')
    sys.exit()
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO')
sleep(0.6)
print('-+' * 10)
print("""My play: {}
Your play: {}""".format(l[pcplay], l[uplay]))
print('-+' * 10)
if pcplay == uplay:
    print("It's a draw.")
elif pcplay == 0 and uplay == 1 or pcplay == 1 and uplay == 2 or pcplay == 2 and uplay == 0:
    print('You win!')
else:
    print('DIE, HUMAN!!!!')
