class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, dado):
        self.itens.append(dado)

    def desempilhar(self):
        if self.itens:
            return self.itens.pop()

    def tamanho(self):
        return len(self.itens)


# Função para calcular média
def media_pilha(pilha):
    if pilha.tamanho() == 0:
        return 0
    return sum(pilha.itens) / pilha.tamanho()


# Teste
p = Pilha()

p.empilhar(10)
p.empilhar(20)
p.empilhar(30)

print("Tamanho da pilha:", p.tamanho())
print("Média dos valores:", media_pilha(p))