from typing import Self


class Carro:
  def __init__(self, marca, modelo, cor):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.velocidade = 0

  def acelerar (self):
    self.velocidade += 10
    print(f"velocidade atual: {self.velocidade} km/h")

  def frear (self):
    self.velocidade -= 10

    if self.velocidade < 0:
      self.velocidade = 0
    
    print(f"velocidade atual: {self.velocidade} km/h")

  def exibir_info(self):
      print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")


lista_carros = []

while True != 5:
  print("\n --- menu ---")
  print("1. cadastrar carro")
  print("2. Exibir informações dos carros")
  print("3. Acelerar carro")
  print("4. Frear carro")
  print("5. Sair")

  escolha = input("escolha um opções: ")
  

  if escolha == "5":
    print("saindo do programa")
    break
  
  elif escolha == "1":
    marca = input("digite a marca do carro: ")
    modelo = input("digite o modelo do carro: ")
    cor = input("digite a cor do carro: ")

    novo_carro = Carro(marca, modelo, cor)
    lista_carros.append(novo_carro)

    print("Cadastrado com sucesso!")

  elif escolha == "2":
    if lista_carros:
      for carro in lista_carros:
        carro.exibir_info()

    else:
      print("não há carros cadastrados")

  elif escolha == "3":
    modelo = input ("digite o modelo do carro que deseja acelerar: ")

    for carro in lista_carros:
      if carro.modelo == modelo:
        carro.acelerar()
        break
      else:
        print("modelo não encontrado")

  elif escolha == "4":
    modelo = input ("digite o modelo do carro que deseja frear: ")
    for carro in lista_carros:
      if carro.modelo == modelo:
        carro.frear()
        break
      else:
        print("modelo não encontrado")

  else:
    print("opção invalida")
