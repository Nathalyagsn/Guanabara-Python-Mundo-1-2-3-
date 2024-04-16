NC = str(input('Qual o nome da sua cidade? '))
NCF = NC.strip().lower()  # AQUI EU REMOVI ESPAÇOS EXTRAS E DEIXEI TUDO EM MINUSCULO
if NCF.startswith('santo'):
    print('Começa com Santo.')
else:
    print('Não comeca com Santo.')
