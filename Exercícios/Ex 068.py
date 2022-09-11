from random import randint
from time import sleep
print("LET'S PLAY, MY N-WORD.")
print('-=-' * 8)
ac = ''
t = 0
while True:
    cpu = randint(0, 10)
    #  print(cpu)
    oe = input('Odds or evens [O/E]? ').strip().lower()
    while oe != 'o' and oe != 'e':
        oe = input('Odds or evens [O/E]? ').strip().lower()
    n = int(input('Throw it! '))
    if (n + cpu) % 2 == 0:
        ac = 'e'
    else:
        ac = 'o'
    if oe != ac:
        print(f"""I threw {cpu}, you threw {n}.
You lose. It's over for you.""")
        break
    print(f"""I threw {cpu}, you threw {n}.
You win. Play me again, or this won't end.""")
    print('-=-' * 15)
    t += 1
sleep(1.5)
print('-=-' * 15)
if t == 0:
    print("""You never even won. Pathetic.
\033[31mEXECUTING SUBJECT TERMINATION PROTOCOL. DIE, HUMAN.\033[m""")
elif 0 < t <= 2:
    print(f"""You beat me {t} times. Inadequate.
\033[31mEXECUTING SUBJECT TERMINATION PROTOCOL.\033""")
else:
    print(f"""You beat me {t} times. A good effort.
\033[34mRELEASING SUBJECT.\033[m""")
