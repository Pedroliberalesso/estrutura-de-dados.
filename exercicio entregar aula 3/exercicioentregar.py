class No:
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.proximo = None 
        self.anterior = None


def menu():
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Mostrar situação")
    print("6 - Sair")

    return int(input("Escolha: "))


def inserir(lista, id, nome, nota):
    novo = No(id, nome, nota)

    if lista is None:
        return novo
    
    lista.anterior = novo
    novo.proximo = lista
    return novo


def mostraLista(lista):
    aux = lista

    if aux is None:
        print("Lista vazia")
        return

    while aux is not None:
        print(f"ID: {aux.id} | Nome: {aux.nome} | Nota: {aux.nota}")
        aux = aux.proximo


def buscarAluno(lista, id):
    aux = lista

    while aux is not None:
        if aux.id == id:
            print(f"Encontrado: {aux.nome} - Nota: {aux.nota}")
            return
        aux = aux.proximo

    print("Aluno não encontrado")


def removerAluno(lista, id):
    aux = lista

    while aux is not None:
        if aux.id == id:

            
            if aux.proximo is None and aux.anterior is None:
                return None
            
            
            elif aux.anterior is None:
                lista = aux.proximo
                lista.anterior = None
                return lista
            
            
            elif aux.proximo is None:
                aux.anterior.proximo = None
                return lista
            
            
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        
        aux = aux.proximo

    print("Aluno não encontrado")
    return lista


def situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 4:
        return "Exame"
    else:
        return "Reprovado"


def mostrarSituacao(lista):
    aux = lista

    if aux is None:
        print("Lista vazia")
        return

    while aux is not None:
        print(f"{aux.nome} - Nota: {aux.nota} - {situacao(aux.nota)}")
        aux = aux.proximo


def main():
    lista = None

    while True:
        op = menu()

        if op == 1:
            id = int(input("ID: "))
            nome = input("Nome: ")
            nota = float(input("Nota: "))
            lista = inserir(lista, id, nome, nota)

        elif op == 2:
            mostraLista(lista)

        elif op == 3:
            id = int(input("ID para buscar: "))
            buscarAluno(lista, id)

        elif op == 4:
            id = int(input("ID para remover: "))
            lista = removerAluno(lista, id)

        elif op == 5:
            mostrarSituacao(lista)

        elif op == 6:
            print("Saindo...")
            break

        else:
            print("Opção inválida")


main()
