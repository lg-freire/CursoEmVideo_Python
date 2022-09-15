player = {'name': input('Player name: '), 'games': int(input('# of matches: '))}
goals = []

for i in range(1, player['games']+1):
    goals.append(int(input(f'How many goals scored in match #{i}: ')))

player['goals'] = goals
player['total'] = sum(goals)
print('-=' * 40)
print(player)
print('-=' * 40)
print(f"""Player: {player['name']}
Goals by game, in order: {player['goals']}
Total goals: {player['total']}""")
print('-=' * 40)

print(f"The player {player['name']} has played {player['games']} match(es).")
for c, i in enumerate(player['goals']):
    print(f"    => In his #{c+1} match, he scored {i} goal(s).")
print(f'He scored a total of {player["total"]} goal(s).')
