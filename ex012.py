preço = float(input('qual o valor do produto? R$'))
novo = preço -(preço * 5 / 100)
print('o produto de R${} com o desconto de 5% ele custara {}.'.format(preço,novo))