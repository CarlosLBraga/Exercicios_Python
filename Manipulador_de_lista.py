from time import sleep

class manipulador_lista:
    def __init__(self):
      self.lista = []

    
    def adicionar_elemento (self, elemento):
      self.lista.append(elemento)
      print("elemento", elemento, "adicionado")

    def remover_elemento (self, elemento):
       
       if elemento not in self.lista:
          print("elemento", elemento, "não encontrado")
          return

       self.lista.remove(elemento)
       print("elemento", elemento, "removido")

    def maior_lista (self):
        if len(self.lista) == 0:
          print("Lista Vazia")
        
        else:
            maior = self.lista[0]

            for i in range (1, len(self.lista)):
              if self.lista[i] > maior:
                 maior = self.lista[i]

            print(f"{maior} é o maior elemento da lista")

    def menor_lista (self):
        if len(self.lista) == 0:
          print("Lista Vazia")
        
        else:
            menor = self.lista[0]

            for i in range (1, len(self.lista)):
              if self.lista[i] < menor:
                 menor = self.lista[i]

            print(f"{menor} é o menor elemento da lista")

    def media_lista (self):
        if len(self.lista) == 0:
          print("Lista Vazia")

        else:
            media = 0
            for i in range (0, len(self.lista)):
               media += self.lista[i]

            print("A Média dos valores da lista é: ", media/len(self.lista))
                             

    def exibir_lista (self):
       print(f"{self.lista}")


def menu():
   print("1 - adicionar elemento na lista")
   print("2 - remover elemento da lista")
   print("3 - encontrar maior elemento da lista")
   print("4 - encontrar menor elemento da lista")
   print("5 - calcular a média da lista")
   print("6 - exibir lista atual")
   print("0 - sair")

lista = manipulador_lista()

while True:
    menu()
    
    op = int(input("digite uma opção "))
    if op == 0:
        print("Encerrando o programa")
        for i in range (3):
            print(i+1)
            sleep(0.5)
        break

    elif op == 1:
       sleep(0.5)
       elemento = int(input("digite o elmento que deseja adicionar na lista; "))
       lista.adicionar_elemento(elemento)

    elif op == 2:
       sleep(0.5)
       elemento = int(input("digite o elemento que deseja remover da lista"))
       print("-" * 30)
       lista.remover_elemento(elemento)
       print("-" * 30)

    elif op == 3:
       print("-" * 30)
       lista.maior_lista()
       print("-" * 30)

    elif op == 4:
        print("-" * 30)
        lista.menor_lista()
        print("-" * 30)
    
    elif op == 5:
       print("-" * 30)
       lista.media_lista()
       print("-" * 30)

    elif op == 6:
       sleep(0.5)
       print("Exibindo a lista")
       lista.exibir_lista()

    else:
       print("-" * 30)
       print("Opção Inválida")
       print("-" * 30)
