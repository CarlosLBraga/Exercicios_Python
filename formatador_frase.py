class formatador_frase:
    def __init__(self, frase):
        self.frase = frase

    def formatar_maiusculas (self):
        self.frase = self.frase.upper()

    def formatar_minusculas (self):
        self.frase = self.frase.lower()

    def formatar_capitalize (self):
        self.frase = self.frase.capitalize()

    def formatar_titulo (self):
        self.frase = self.frase.title()

    def limpa_frase (self):
        return ''.join(self.frase.lower().split())

    def contar_vogal (self):
        vogais = 'aeiouáéíóúàèìòùãõâêô'
        cont = 0
        frase_minuscula = self.frase.lower()
        for letra in frase_minuscula:
            if letra in vogais:
                cont += 1
        
        return cont

    def contar_consoantes (self):
        frase = self.limpa_frase()
        vogais = 'aeiouáéíóúàèìòùãõâêô'
        cont = 0

        for letra in frase:
            if letra not in vogais:
                cont += 1
        
        return cont

    def contar_a (self):

        letra_a = 'aáãâà'
        cont = 0
        frase = self.frase.lower()
        for a in frase:
            if a in letra_a:
                cont += 1

        return cont

    def procurar_palavra (self, palavra):
        return self.frase.lower().count(palavra.lower())

    def retornar_frase (self):
        return self.frase


def menu():
    print("Bem Vindo ao formatador de frase ")
    frase = input("digite uma frase: ")
    formatador = formatador_frase(frase)

    while True:
        print("escolha uma opção ")
        print("1 - Converter para maiúsculas ")
        print("2 - Converter para Minúsculas ")
        print("3 - Capitalizar a primeiro letra da frase ")
        print("4 - Converter para formato de título ")
        print("5 - contar vogais ")
        print("6 - Contar Consoantes ")
        print("7 - Contar letra 'a' ")
        print("8 - Pesquisar Palavra ")
        print("9 - para sair ")

        op = int(input("digite a opção: "))

        if op == 9:
            print("Finalizando o programa ... ")
            break

        elif op == 1:
            formatador.formatar_maiusculas()

        elif op == 2:
            formatador.formatar_minusculas()

        elif op == 3:
            formatador.formatar_capitalize()

        elif op == 4:
            formatador.formatar_titulo()
        
        elif op == 5:
            print(f"Sua Frase Possui: {formatador.contar_vogal()} Vogais")

        elif op == 6:
            print(f"Total de Consoantes: {formatador.contar_consoantes()}")

        elif op == 7:
            print(f"a letra 'A' apareceu {formatador.contar_a()} vezes ")

        elif op == 8:
            palavra = input("Digite a Palavra que você deseja procurar: ")
            cont = formatador.procurar_palavra(palavra)
            
            if cont > 0:
                print(f"A palavra {palavra} aparece {cont} na frase")
            else:
                print("Palavra não encontrada !!!")

        else:
            print("Opção Inválida")
            

        print("---" * 30)
        print(f"frase atual: {formatador.retornar_frase()}")
        print("---" * 30)



menu()
