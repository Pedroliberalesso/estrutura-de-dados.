class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, dado):
        self.itens.append(dado)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            print("Pilha vazia!")

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            print("Pilha vazia!")

    def esta_vazia(self):
        return len(self.itens) == 0


# Teste
p = Pilha()

p.empilhar(5)
p.empilhar(15)
p.empilhar(25)

print("Topo:", p.topo())

p.desempilhar()

print("Topo depois de remover:", p.topo())