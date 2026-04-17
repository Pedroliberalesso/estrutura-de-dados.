class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, dado):
        self.itens.append(dado)

    def desempilhar(self):
        if len(self.itens) > 0:
            return self.itens.pop()
        else:
            print("Pilha vazia!")

    def percorrer(self):
        print("Elementos da pilha:")
        for item in reversed(self.itens):
            print(item)


# Teste
p = Pilha()

p.empilhar(10)
p.empilhar(20)
p.empilhar(30)

p.desempilhar()  

p.percorrer()