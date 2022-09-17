from MyFunctions import title


def table(j='<blank>', g=0):
    return f'Player {j} has scored {g} goals.'


title('PLAYER SCORE', 30)
player = input('Player name: ')
goals = input('Goals scored: ')

goals = int(goals) if goals.isnumeric() else 0

if player:
    print(table(player, goals))
else:
    print(table(g=goals))
