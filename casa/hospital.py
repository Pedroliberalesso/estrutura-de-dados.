class No:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade  # emergencia, urgente, normal
        self.proximo = None
        self.anterior = None


def inserir(lista, nome, idade, prioridade):
    novo = No(nome, idade, prioridade)

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


def listar(lista):
    if lista is None:
        print("Nenhum paciente na fila.")
        return

    aux = lista
    while True:
        print(f"{aux.nome} | {aux.idade} anos | {aux.prioridade}")
        aux = aux.proximo
        if aux == lista:
            break


def buscar_prioridade(lista, prioridade):
    if lista is None:
        return None

    aux = lista
    while True:
        if aux.prioridade == prioridade:
            return aux
        aux = aux.proximo
        if aux == lista:
            break

    return None


def atender(lista):
    print("\n Início dos atendimentos...\n")

    while lista is not None:
        # prioridade: emergência > urgente > normal
        paciente = buscar_prioridade(lista, "emergencia")

        if paciente is None:
            paciente = buscar_prioridade(lista, "urgente")

        if paciente is None:
            paciente = buscar_prioridade(lista, "normal")

        print(f"🩺 Atendendo: {paciente.nome} ({paciente.prioridade})")

        lista = remover(lista, paciente)

    print("\n Todos os pacientes foram atendidos!")
    return None


def menu():
    print("\n--- TRIAGEM HOSPITALAR ---")
    print("1 - Inserir paciente")
    print("2 - Listar pacientes")
    print("3 - Iniciar atendimento")
    print("4 - Sair")
    return int(input("Escolha: "))



lista = None

while True:
    opc = menu()

    if opc == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        prioridade = input("Prioridade (emergencia/urgente/normal): ").lower()

        lista = inserir(lista, nome, idade, prioridade)

    elif opc == 2:
        listar(lista)

    elif opc == 3:
        if lista is None:
            print("Fila vazia!")
        else:
            lista = atender(lista)

    elif opc == 4:
        print("Encerrando sistema...")
        break