li = ('Thots', 'Carnivore', 'Jabroni', 'Pauper', 'Semblance', 'Arrakis', 'Dune', 'Chapterhouse', 'Simple')
for word in li:
    print(f'The vowels of the word {word} are ', end='')
    for i in range(0, len(word)):
        if word[i] in 'AaEeIiOoUu':
            print(word[i], end=' ')
    print('')
