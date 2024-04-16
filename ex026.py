LA = str(input('Digite uma frase para verificar a letra A: ')).lower().strip()
print('A letra A aparece: {} vezes'.format(LA.count('a'))) #aqui conta quantas letras A tem
print('A primeira letra A aparece na posição: {}'.format(LA.find('a')+1)) #aqui encontrou o primeiro A
print('A ultima letra A aparece na posição: {}'.format(LA.rfind('a')+1)) #aqui achou no final
