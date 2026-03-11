class Aluno:

    def __init__ (self, nome, frequencia, MediaGeral):
        self.nome = nome
        self.frequencia = frequencia
        self.MediaGeral = MediaGeral

    def MostrarDados (self):
        print("Nome:", self.nome)    
        print("Media =", self.MediaGeral)
        print("frequencia", self.frequencia)

aluno1 = Aluno("Joao", 76, 7.8)
aluno2 = Aluno("Maria", 80, 8.5)

aluno1.MostrarDados()
aluno2.MostrarDados ()