class Livro:
    def __init__(self,autor, numpag):
        self.autor= autor
        self.numpag= numpag

    def calcular(self):
        if self.numpag <=100:
            print("o livro de",self.autor,"é curto")
        else:
             print("o livro de",self.autor,"é longo")
            




l1 = Livro("fulano", 90)
l2 = Livro("ciclano",150)

l1.calcular()
l2.calcular()