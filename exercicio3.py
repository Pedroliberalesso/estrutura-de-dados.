class Produto:

    def __init__(self,nome, preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.ValorStock = 0

    def calcular(self):
        self.ValorStock = self.preco * self.quantidade

        
 
    def mostrardado(self):
        print("Valor total do produto", self.nome,'é =', self.ValorStock)
    


produto1 = Produto("açucar", 10, 10)

produto1.calcular()
produto1.mostrardado()

    
