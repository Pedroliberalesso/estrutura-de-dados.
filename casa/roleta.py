class No:
    def __init__(self, id):
        self.id = id
        self.proximo = None
        self.anterior = None

seed = 7

def pseudo_rand(maximo):
    global seed
    seed = (seed * 1103515245 + 12345) % (2**31)
    return seed % maximo


def inserir(lista, id):
    novo = No(id)

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


def listar(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    while True:
        print(f"Guerreiro {aux.id}")
        aux = aux.proximo
        if aux == lista:
            break


def remover(lista, no):
    if lista is None:
        return None

    if no.proximo == no:
        return None

    no.anterior.proximo = no.proximo
    no.proximo.anterior = no.anterior

    if no == lista:
        lista = no.proximo

    return lista


def obter_no_por_indice(lista, indice):
    aux = lista
    for _ in range(indice):
        aux = aux.proximo
    return aux


def tamanho_lista(lista):
    if lista is None:
        return 0

    cont = 0
    aux = lista
    while True:
        cont += 1
        aux = aux.proximo
        if aux == lista:
            break

    return cont


def roleta_russa(lista):
    print(" Início do jogo!")

    while tamanho_lista(lista) > 1:
        tam = tamanho_lista(lista)

        indice = pseudo_rand(tam) 

        eliminado = obter_no_por_indice(lista, indice)

        print(f" Eliminado: Guerreiro {eliminado.id}")

        lista = remover(lista, eliminado)

    print(f"\n🏆 Sobrevivente: Guerreiro {lista.id}")


def menu():
    print("\n--- ROLETA RUSSA ---")
    print("1 - Adicionar guerreiros")
    print("2 - Listar guerreiros")
    print("3 - Iniciar jogo")
    print("4 - Sair")
    return int(input("Escolha: "))



lista = None

while True:
    opc = menu()

    if opc == 1:
        qtd = int(input("Quantos guerreiros deseja adicionar: "))
        for i in range(1, qtd + 1):
            lista = inserir(lista, i)

    elif opc == 2:
        listar(lista)

    elif opc == 3:
        if lista is None:
            print("Adicione guerreiros primeiro!")
        else:
            roleta_russa(lista)
            lista = None

    elif opc == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")