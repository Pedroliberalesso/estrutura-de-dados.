class Produto:

    def __init__ (self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade


    def MostrarDados (self, quantidadefinal):
        print("Nome:", self.nome)    
        print("preço =", self.preço)
        print("quantidade", self.quantidade)
        print("quantidade final =",quantidadefinal )

    def adicionar(self):
        quantidadeadc = int(input("unidades novas"))
        quantidadefinal = quantidadeadc + self.quantidade
        return  quantidadefinal

produto1 = Produto("cafe", 20, 50)
produto2 = Produto("açucar", 15, 70)



qf1= produto1.adicionar()
qf2= produto2.adicionar()
produto1.MostrarDados(qf1)
produto2.MostrarDados(qf2)
