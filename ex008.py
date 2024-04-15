medida = float(input('Digite uma distancia em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
print('A conversão em cm é: {} cm\nEm mm é: {} mm\nEm km é: {} km\nEm dm é: {} dm\nEm hm é:{} hm\nEm dam é: {} dam' .format(cm, mm, km, dm, hm, dam))
