class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None


def InserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista 
    lista  = novoItem
    return lista


def listarItens(lista):
    aux = lista

    if aux is None:
        print("Lista vazia")
        return

    while aux is not None:
        print("Item:", aux.item)
        aux = aux.proximo


def excluirItem(lista , item):
    aux = lista
    anterior = None
    
    if aux is None:
        print("lista vazia")


    while aux.item == item:
        if lista == aux:
            lista = lista.proximo
            return lista
        
        elif aux.proximo == None:
            anterior.proximo = None 
            return lista
        
        else:
            anterior == aux
            anterior.proximo = aux.proximo
            return lista



def maiores(lista, maior):
    aux = lista
    encontrou = False

    while aux is not None:
        if aux.item > maior:
            print(aux.item)
            encontrou = True
        aux = aux.proximo

    if encontrou == False:
        print("Nenhum número maior encontrado")


def menu():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Excluir item")
    print("4 - verificar itens")
    print("5 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc


def main():
    lista = None
    opc = 0


    while opc != 5:
        opc = menu()

        if opc == 1 :
            item = int(input("digite um item a ser adc:"))
            lista = InserirItem(lista , item)

        if opc == 2:

            listarItens(lista)

        if opc == 3:
            item = int(input("Digite um item para excluir:"))
            lista = excluirItem(lista, item)

        if opc == 4:    
            maior = int(input("numero que deseja verificar:"))
            lista = maiores(lista, maior)




main()



    


