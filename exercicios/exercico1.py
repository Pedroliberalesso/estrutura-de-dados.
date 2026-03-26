class No:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.proximo = None
        self.anterior = None


def inserir(lista, id, nome):
    novo = No(id, nome)

    if lista is None:
        return novo

    aux = lista
    while aux.proximo:
        aux = aux.proximo

    aux.proximo = novo
    novo.anterior = aux

    return lista


def listar(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    while aux:
        print(f"ID: {aux.id} | Nome: {aux.nome}")
        aux = aux.proximo


def remover(lista, id):
    if lista is None:
        print("Lista vazia!")
        return lista

    aux = lista

    while aux:
        if aux.id == id:
           
            if aux.anterior is None:
                lista = aux.proximo
                if lista:
                    lista.anterior = None
            else:
                aux.anterior.proximo = aux.proximo
                if aux.proximo:
                    aux.proximo.anterior = aux.anterior

            print("Removido com sucesso!")
            return lista

        aux = aux.proximo

    print("ID não encontrado!")
    return lista


def buscar_id(lista, id):
    aux = lista
    while aux:
        if aux.id == id:
            return aux
        aux = aux.proximo
    return None


def buscar_nome(lista, nome):
    aux = lista
    while aux:
        if aux.nome.lower() == nome.lower():
            return aux
        aux = aux.proximo
    return None


def menu():
    print("  --- MENU ---")
    print("1 - Inserir nó")
    print("2 - Listar nós")
    print("3 - Remover nó")
    print("4 - Verificar se nó existe")
    print("5 - Sair")
    return int(input("Escolha: "))


def menu_busca():
    print("--- BUSCAR ---")
    print("1 - Por ID")
    print("2 - Por Nome")
    return int(input("Escolha: "))



lista = None

while True:
    opc = menu()

    if opc == 1:
        id = int(input("Digite o ID: "))
        nome = input("Digite o nome: ")
        lista = inserir(lista, id, nome)

    elif opc == 2:
        listar(lista)

    elif opc == 3:
        id = int(input("Digite o ID para remover: "))
        lista = remover(lista, id)

    elif opc == 4:
        opc_busca = menu_busca()

        if opc_busca == 1:
            id = int(input("Digite o ID: "))
            no = buscar_id(lista, id)
        else:
            nome = input("Digite o nome: ")
            no = buscar_nome(lista, nome)

        if no:
            print(f"Encontrado -> ID: {no.id}, Nome: {no.nome}")
        else:
            print("Nó não encontrado!")

    elif opc == 5:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")