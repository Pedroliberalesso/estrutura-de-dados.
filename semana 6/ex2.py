class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


ret = Retangulo(5, 3)

print(f"Área: {ret.area()}")
print(f"Perímetro: {ret.perimetro()}")