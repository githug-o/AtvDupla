def cadastrar_contatos(contatos,nome,telefone, email):
    contato = {
        'Nome':nome,
        'Telefone':telefone,
        'E-mail':email,
        
    }
    contatos.append(contato)
    print(f"")
    print("Contato cadastrado mermão!!")
    print(f"****************************")
    print(f"")

def imprimir_contatos(contatos):
    for indice,contato in enumerate(contatos):
        print(f"****************************")
        print(f"ID do contato:    {indice+1}")
        print(f"Nome:  {contato['Nome']}")
        print(f"Telefone:  {contato['Telefone']}")
        print(f"E-mail:  {contato['E-mail']}")
       
        print(f"****************************")
        print(f"")
   
def deletar_contatos(contatos, indice):
    if 0 <= indice <= len(contatos):
        del contatos[indice]
        print("Contato apagado")
    else:
        print("Contato não encontrado!")

def editar_contatos(contatos, indice):
    if 0 <= indice <= len(contatos):
              
        print(f"****************************")
        print("")
        contatos[indice]['Nome'] = input("Digite o novo nome do contato: ")
        contatos[indice]['Telefone'] = input("Digite o novo telefone do contato: ")
        contatos[indice]['E-mail'] = input("Digite o novo e-mail do contato: ")

        print("Contato atualizado!")
        print(f"****************************")
        print("")
    else:
        print("ID de contato não encontrado!")
contatos = []

while True:
    opc = int(input("Olá, bem vindo a lista de contatos \n"
                    " Escolha uma opção: \n" 
                    "1 - Cadastrar contato; \n"
                    "2 - Imprimir contatos cadastrados; \n"
                    "3 - Editar contatos; \n"
                    "4 - Deletar contato; \n"
                    "5 - Sair... Bye bye \n"))

    if opc == 1:

        nome = input("Digite o nome:    ")
        telefone = input("Digite o número de telefone:    ")
        email = input("Digite o e-mail do arrombado:    ")
        
        cadastrar_contatos(contatos, nome, telefone, email)
    elif opc == 2:
        imprimir_contatos(contatos)
    elif opc == 3:
        indice = int(input("Digite o ID do contato: "))-1
        editar_contatos(contatos, indice)
    elif opc == 4:
        indice = int(input("Digite o ID do contato: "))-1
        deletar_contatos(contatos, indice)
    else:
        print("Até logo caro amigo contato, estarei esperando ancioso pelo seu retorno! \n")
        break
