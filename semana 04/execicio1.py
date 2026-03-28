class No:
    def __init__(self, id, bastao=False):
        self.id = id
        self.bastao = bastao
        self.proximo = None
        self.anterior = None


def inserir(lista, id, bastao=False):
    novo = No(id, bastao)

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
        print("Lista vazia")
        return

    aux = lista
    while True:
        print(f"Atleta {aux.id} | Bastão: {aux.bastao}")
        aux = aux.proximo
        if aux == lista:
            break


def remover(lista, id):
    if lista is None:
        return None

    aux = lista
    while True:
        if aux.id == id:
            if aux == aux.proximo:  
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = lista.proximo

            return lista

        aux = aux.proximo
        if aux == lista:
            print("Atleta não encontrado")
            return lista


def passar_bastao(lista, voltas):
    if lista is None:
        print("Lista vazia")
        return


    atual = lista
    while not atual.bastao:
        atual = atual.proximo
        if atual == lista:
            print("Nenhum atleta está com o bastão!")
            return

    print("\n--- Simulação ---")

    for i in range(voltas):
        print(f"Turno {i+1}: Atleta {atual.id} está com o bastão")

    
        atual.bastao = False
        atual = atual.proximo
        atual.bastao = True


def main():
    lista = None

    lista = inserir(lista, 1, True) 
    lista = inserir(lista, 2)
    lista = inserir(lista, 3)
    lista = inserir(lista, 4)

    print("Lista inicial:")
    listar(lista)

    passar_bastao(lista, 10)

main()