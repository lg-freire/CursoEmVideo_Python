frase = input('Present a sentence: ')
print('Instances of letter "A": {}'.format(frase.lower().count('a')))
print('First letter "A" in {} position.'.format(frase.lower().find('a')))
print('Last letter "A" in {} position.'.format(frase.lower().rfind('a')))
