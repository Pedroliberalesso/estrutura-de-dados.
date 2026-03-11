class contato:
    def __init__(self,nome ,telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

agenda = []
agenda.append (contato("Marcos", "9999-1111", "marcos@email.com"))
agenda.append (contato("Maria", "9888-2222", "maria@email.com"))


for contato in agenda:
    print("nome-", contato.nome,"-" , contato.telefone)