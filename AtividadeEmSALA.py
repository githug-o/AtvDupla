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

contatos = []

while True:
    opc = int(input(f"Olá, bem vindo a lista de contatos \n Escolha uma opção: \n 1 - Cadastrar contato; \n 2 - Imprimir contatos cadastrados; \n 3 - Editar contatos; \n  4 - Deletar contato; \n 5 - Sair... Bye bye "))

    if opc == 1:

        nome = input("Digite o nome:    ")
        telefone = float(input("Digite o número de telefone:    "))
        email = int(input("Digite o e-mail do arrombado:    "))
        

        cadastrar_contatos(contatos, nome, telefone, email)
    elif opc == 2:
        imprimir_contatos(contatos)
    elif opc == 3:
        editar_contatos(contatos, indice, nome, telefone, email)
    elif opc == 4:
        deletar_contatos()
    else:
        break