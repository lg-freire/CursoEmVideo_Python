frase = input('Present a sentence: ').lower().strip()
print('Instances of letter "A": {}'.format(frase.count('a')))
print('First letter "A" in {} position.'.format(frase.find('a')+1))  # +1 so the user won't be returned a zero
print('Last letter "A" in {} position.'.format(frase.rfind('a')+1))
