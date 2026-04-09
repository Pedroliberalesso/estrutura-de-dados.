class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


def inserir(lista, nome):
    novo = No(nome)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    ultimo = lista.anterior

    ultimo.proximo = novo
    novo.anterior = ultimo

    novo.proximo = lista
    lista.anterior = novo

    return lista


def remover(lista, nome):
    if lista is None:
        print("Lista vazia!")
        return None

    aux = lista

    while True:
        if aux.nome == nome:
            # só um cliente
            if aux.proximo == aux:
                print(f"{nome} saiu.")
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

            print(f"{nome} saiu.")
            return lista

        aux = aux.proximo
        if aux == lista:
            break

    print("Cliente não encontrado!")
    return lista


def listar(lista):
    if lista is None:
        print("Nenhum cliente.")
        return

    aux = lista
    while True:
        print(aux.nome)
        aux = aux.proximo
        if aux == lista:
            break


def passar_pizza(lista, voltas):
    if lista is None:
        print("Nenhum cliente para receber pizza.")
        return

    atual = lista

    print("\n Pizza começou a circular!\n")

    for i in range(voltas):
        print(f"👉 {atual.nome} recebeu a fatia")
        atual = atual.proximo


def menu():
    print("\n--- RODÍZIO DE PIZZA ---")
    print("1 - Adicionar cliente")
    print("2 - Remover cliente")
    print("3 - Listar clientes")
    print("4 - Passar pizza")
    print("5 - Sair")
    return int(input("Escolha: "))


lista = None

while True:
    opc = menu()

    if opc == 1:
        nome = input("Nome do cliente: ")
        lista = inserir(lista, nome)

    elif opc == 2:
        nome = input("Nome para remover: ")
        lista = remover(lista, nome)

    elif opc == 3:
        listar(lista)

    elif opc == 4:
        voltas = int(input("Quantas pessoas vão receber a pizza: "))
        passar_pizza(lista, voltas)

    elif opc == 5:
        print("Encerrando rodízio...")
        break

    else:
        print("Opção inválida!")