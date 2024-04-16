N = str(input('Digite um número: '))      #só funciona com exatamente 4 numeros
NS = N.replace("", " ")
NL = NS.split()
print('A milhar é: {}'.format(NL[ 0 ]))
print('A centena é: {}'.format(NL[ 1 ]))
print('A dezena é: {}'.format(NL[ 2 ]))
print('A uniadade é: {}'.format(NL[ 3 ]))
