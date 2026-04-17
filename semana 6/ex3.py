class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")


carro1 = Carro("Toyota", "Corolla", 2022)

carro1.ligar()
carro1.desligar()