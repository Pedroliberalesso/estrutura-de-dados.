class alunos:

    def __init__(self,nome,n1,n2,n3):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3


    def verificarAprovaçao (self):
        media = (self.n1 + self.n2 + self.n3)
        media = (media / 3)
        return media

    def MostrarDados (self, media):
        if media <= 7:
            print("o aluno",self.nome, "foi reprovado com media", media)

        else:
            print("o aluno", self.nome, "foi aprovado com media de", media)

aluno1 = alunos("joao", 3 , 5, 6)
aluno2 = alunos("maria", 7 , 8, 9)

m1 = aluno1.verificarAprovaçao()
m2 = aluno2.verificarAprovaçao()
aluno1.MostrarDados(m1)
aluno2.MostrarDados(m2)