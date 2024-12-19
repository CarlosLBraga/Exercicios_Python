#quem nunca teve que fazer a tabuada quando era mais novo?
#algoritmo para fazer uma tabuada usando for

while True:
    n = int(input('Qual tabuada você gostaria de ver? '))
    for cont in range (1, 11):
       print (f'{n} x {cont} = {n*cont}')