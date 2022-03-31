co = float(input(' comprimento do cateto oposto :'))
ca = float(input('comprimento do cateto adiacente :'))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('a hipotenusa vale {:.2f}'.format(hi))