import math
An = int(input('Digite um angulo: '))
rad = math.radians(An)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O seno: {:.2f}\nConsseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))
