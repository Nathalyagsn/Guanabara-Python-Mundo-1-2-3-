from math import sqrt
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
x = (co**2 + ca**2)
raiz = sqrt(x)
print('O comprimento da hipotenusa é: {:.2f}'.format(raiz))
