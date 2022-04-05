frase = str(input('informe uma frase :')).strip()
print('a letra A aparece {} na frase.'.format(frase.count('a')))
print('a letra A aparece na posição {} na primeira vez'.format(frase.find('a')))
print('a letra A aparece na posição {} na ultima vez.'.format(frase.rfind('a')))
