class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None


def menu():
    print(" - Adicionar parada")
    print("2 - Listar paradas")
    print("3 - Remover parada")
    print("4 - Simular percurso")
    print("5 - Sair")
    return int(input("Escolha uma opção: "))


def inserir(lista, parada):
    novo = No(parada)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    lista.anterior.proximo = novo
    novo.anterior = lista.anterior
    lista.anterior = novo
    novo.proximo = lista

    return lista


def listar(lista):
    if lista is None:
        print("Nenhuma parada cadastrada")
        return

    aux = lista
    while True:
        print("Parada:", aux.parada)
        aux = aux.proximo
        if aux == lista:
            break


def remover(lista, parada):
    if lista is None:
        print("Lista vazia")
        return None

    aux = lista
    while True:
        if aux.parada == parada:

        
            if aux == aux.proximo:
                print("Última parada removida")
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = lista.proximo

            print("Parada removida com sucesso")
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Parada não encontrada")
            return lista


def simular_percurso(lista, passos):
    if lista is None:
        print("Sem paradas na rota")
        return

    aux = lista
    print("\n--- Percurso do ônibus ---")

    for i in range(passos):
        print(f"Parada {i+1}: {aux.parada}")
        aux = aux.proximo


def main():
    lista = None
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            parada = input("Digite o nome da parada: ")
            lista = inserir(lista, parada)

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:
            parada = input("Digite a parada a remover: ")
            lista = remover(lista, parada)

        elif opcao == 4:
            passos = int(input("Quantas paradas deseja simular? "))
            simular_percurso(lista, passos)

    print("Encerrado!")


main()