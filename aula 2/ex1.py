class No:
    def __init__(self ,item   ):
        self.item = item
        self.proximo = None

    def inserirItem (lista, item):
        NovoItem = No(item)
        NovoItem.proximo = lista
        lista = NovoItem

    def ListarItens(lista):
        aux = lista 

        if aux == None:
            print("lista vazia")
            return
        while aux is not None:
            print("Item", )


    def menu():
        print("1 - inserir item")
        print("2 - listar intem")
        print("3 - executar intem")
        print("4 - sair")
        opc = int(input("escolhe uma opc"))
        return opc
    
    def main():
        lista = None
        opc = 0

        while opc != 4:
            opc = menu():

        if opc == 1:
            item = int(input("digite um item a inserir"))
            lista = inserirItem(lista, item):

