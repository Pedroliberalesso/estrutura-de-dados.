class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def bonus(self):
        if self.cargo == "Gerente":
            adicional = self.salario * 0.10
        else:
            adicional = self.salario * 0.05
        return adicional

    def mostardados(self, adicional):
        salario_com_bonus = self.salario + adicional
        print("O cargo do", self.nome, "é", self.cargo, 
              "recebendo adicional de", adicional,
              "e salário com bônus de", salario_com_bonus)


func1 = Funcionario("Marco", 2000, "Pião")
func2 = Funcionario("Joao", 5000, "Gerente")

bonus1 = func1.bonus()
bonus2 = func2.bonus()

func1.mostardados(bonus1)
func2.mostardados(bonus2)