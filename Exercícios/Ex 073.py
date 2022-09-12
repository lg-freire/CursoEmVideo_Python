teams = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Atheltico PR', 'Atlético-MG',
         'América-MG', 'Goiás', 'Santos', 'Red Bull Bragantino', 'Botafogo', 'São Paulo', 'Ceará', 'Fortaleza',
         'Cuiabá-MT', 'Avaí', 'Atlético-GO', 'Juventude')
print('\033[34mTimes na zona de classificação:\033[m')
for i in range(0,5):
    print(f'#{i+1}: {teams[i]}')
print('\033[31mTimes na zona de rebaixamento:\033[m')
for i in range(-4, 0):
    print(f'#{i+21}: {teams[i]}')
print(f'\033[35mOs times na tabela são\n\033[m{sorted(teams)}')
print(f"O \033[32mPalmeiras\033[m está na posição #{teams.index('Palmeiras')+1}")
