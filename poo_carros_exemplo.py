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


carro1 = Carro("Toyota", "Corolla", "Branca")
carro1.exibir_info()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()

print("--------------------------")

carro2 = Carro("Ford", "Fiesta", "Preto")

carro2.exibir_info()
carro2.acelerar()
carro2.acelerar()
