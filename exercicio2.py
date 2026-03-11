class Produto:

    def __init__ (self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def MostrarDados (self):
        print("Nome:", self.nome)    
        print("preço =", self.preço)
        print("quantidade", self.quantidade)

produto1 = Produto("cafe", 20, 50)
produto2 = Produto("açucar", 15, 70)

produto1.MostrarDados()
produto2.MostrarDados()
