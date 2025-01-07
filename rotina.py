class pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.acordado = False
        self.comendo = False
        self.dirigindo = False


    def acordar (self):
        if self.acordado:
            print(f"{self.nome} já está acordado")
        
        else:

            self.acordado = True
            print(f"{self.nome} acordou :D")
    
    def comer (self):
        if self.dirigindo:
            print(f"{self.nome} está dirigindo e não pode comer")
        
        elif not self.acordado:
            print(f"{self.nome} ainda não está acordado")

        else:
            self.comendo = True
            print(f"{self.nome} está comendo")
    
    def parar_comer (self):
        if self.comer:
            print(f"{self.nome} parou de comer")
            self.comendo = False

        else:
            print(f"{self.nome} ainda não está comendo ")
    
    def dirigir (self):
        if not self.acordado :
            print(F"{self.nome} ainda está dormindo e não pode dirigir")

        elif self.comendo:
            print(f"{self.nome} está comendo e não pode dirigir")


        elif self.dirigindo:
            print(f"{self.nome} já está dirigindo")

        else:
            self.dirigindo = True
            print(f"{self.nome} está digirindo")

    def parar_dirigir(self):
        if self.dirigindo:
            print(f"{self.nome} parou de dirigir.")
            self.dirigindo = False
        else:
            print(f"{self.nome} não está dirigindo.")

cadu = pessoa("Cadu")
cadu.dirigir()
cadu.acordar()
cadu.dirigir()
cadu.comer()
cadu.parar_dirigir()
cadu.comer()
