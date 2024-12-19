p = float(input('digite seu peso em kg: '))
h = float(input('digite sua altura em M: '))

IMC = p / (h ** 2)

print (f'seu IMC é {IMC :.3f} ')

if IMC < 18.5:
    print ('seu IMC está abaixo')

elif IMC <= 24.9:
    print(f'Você está saudável')
elif IMC <= 29.9:
    print(f'peso em excesso')
elif IMC <= 34.9:
    print(f'Obesidade Grau I')
elif IMC <= 39.9:
    print(f'Obesidade Grau II')
else:
    print(f'Obesidade Grau III')