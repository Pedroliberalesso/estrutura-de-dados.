class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = (self.notas[0] + self.notas[1] + self.notas[2]) / 3
        return media

    def verificar_aprovacao(self):
        media = self.calcular_media()

        print("Aluno:", self.nome)
        print("Média:", media)

        if media >= 7:
            print(" Aprovado")
        else:
            print(" Reprovado")


aluno1 = Aluno("João", [8, 7, 9])
aluno2 = Aluno("Maria", [5, 6, 6])

aluno1.verificar_aprovacao()

aluno2.verificar_aprovacao()