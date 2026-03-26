class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None


def inserir(lista, id, nome, artista, duracao):
    novo = No(id, nome, artista, duracao)

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
        print("Playlist vazia!")
        return

    aux = lista
    while aux:
        print(f"[{aux.id}] {aux.nome} - {aux.artista} ({aux.duracao} min)")
        aux = aux.proximo


def remover(lista, id):
    if lista is None:
        print("Playlist vazia!")
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

            print("Música removida!")
            return lista

        aux = aux.proximo

    print("Música não encontrada!")
    return lista


def buscar_nome(lista, nome):
    aux = lista
    while aux:
        if aux.nome.lower() == nome.lower():
            return aux
        aux = aux.proximo
    return None


def buscar_artista(lista, artista):
    aux = lista
    encontrou = False
    while aux:
        if aux.artista.lower() == artista.lower():
            print(f"[{aux.id}] {aux.nome} - {aux.artista} ({aux.duracao} min)")
            encontrou = True
        aux = aux.proximo

    if not encontrou:
        print("Nenhuma música encontrada desse artista.")


def duracao_total(lista):
    total = 0
    aux = lista
    while aux:
        total += aux.duracao
        aux = aux.proximo
    print(f"Duração total: {total} minutos")


def menu():
    print("\n--- PLAYLIST ---")
    print("1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Remover música")
    print("4 - Buscar música")
    print("5 - Duração total")
    print("6 - Próxima música")
    print("7 - Música anterior")
    print("8 - Sair")
    return int(input("Escolha: "))


def menu_busca():
    print("\n1 - Buscar por nome")
    print("2 - Buscar por artista")
    return int(input("Escolha: "))


lista = None
atual = None

while True:
    opc = menu()

    if opc == 1:
        id = int(input("ID: "))
        nome = input("Nome: ")
        artista = input("Artista: ")
        duracao = float(input("Duração (min): "))

        lista = inserir(lista, id, nome, artista, duracao)

        if atual is None:
            atual = lista 

    elif opc == 2:
        listar(lista)

    elif opc == 3:
        id = int(input("ID para remover: "))
        lista = remover(lista, id)

    elif opc == 4:
        op = menu_busca()

        if op == 1:
            nome = input("Nome: ")
            m = buscar_nome(lista, nome)
            if m:
                print(f"Encontrada: {m.nome} - {m.artista}")
            else:
                print("Não encontrada!")
        else:
            artista = input("Artista: ")
            buscar_artista(lista, artista)

    elif opc == 5:
        duracao_total(lista)

    elif opc == 6:
        if atual and atual.proximo:
            atual = atual.proximo
            print(f"Tocando: {atual.nome} - {atual.artista}")
        else:
            print("Não há próxima música.")

    elif opc == 7:
        if atual and atual.anterior:
            atual = atual.anterior
            print(f"Tocando: {atual.nome} - {atual.artista}")
        else:
            print("Não há música anterior.")

    elif opc == 8:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")