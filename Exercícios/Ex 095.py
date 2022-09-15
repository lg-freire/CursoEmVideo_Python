team, goals = [], []
count = 1

while True:
    player = {'name': input(f'Player name #{count}: '), 'games': int(input(f'# of matches: '))}
    for i in range(1, player['games']+1):
        goals.append(int(input(f'How many goals scored in match #{i}: ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    goals.clear()
    team.append(player)
    count += 1
    flag = input('Continue [Y/N]: ').strip().lower()
    while flag not in 'yn':
        flag = input("""\033[31mINVALID INPUT\033[m
Continue [Y/N]: """).strip().lower()
    if flag == 'n':
        break


print('-=' * 40)
print(team)
print(team[0]["name"])
print('-=' * 40)
print(f"{'#':^3}|{'Name':<20}|{'Goals':<30}|Total")
print('-' * 62)
for i in range(0, len(team)):
    print(f"{i+1}  |{team[i]['name']:<20}|{str(team[i]['goals']):<30}|{team[i]['total']:>5}")
print('-' * 62)

while True:
    choice = int(input('Show detailed data for which player (999 to finish program): '))
    if choice == 999:
        print('\033[34mPROGRAM TERMINATED\033[m')
        break
    elif choice-1 > len(team) or choice-1 < 0:
        print('ERROR! There is no such player!')
    elif choice-1 <= len(team):
        print(f'Details of player {team[choice-1]["name"].upper()}: ')
        for i in range(0, len(team[choice-1]['goals'])):
            print(f'In match #{i+1} scored {team[choice-1]["goals"][i]}')
        print('-' * 62)
