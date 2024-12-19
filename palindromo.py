frase = str(input('digite a frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
print(f'{junto}')
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'o inverso de {junto} é {inverso}')
if junto == inverso:
    print('é um palíndromo')
else:
    print('não é um palíndro')