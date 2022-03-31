num = int(input('informe um numero : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' analisando o numero {}.'.format(num))
print('a unidade e {}'.format(u))
print('a dezena e {}'.format(d))
print('a centena e {}'.format(c))
print('a milhar e {}'.format(m))