    #aqui o sistema pede o nome do usuário
    nome= input("me diga seu nome")

    #aqui o sistema pede o nome do usuário
    idade= int(input("me fale sua idade"))

    #aqui mostra o nome e a idade do usuário
    print(f"Bem vindo {nome}, voce tem {idade} anos")

    #aqui é uma função que chama o menu
    def menu():
    print("Como posso te ajudar hoje?")
    print ("1 - bebida")
    print (" 2 - salgados")
    print ("3 - docess")

    opc_user = int(input("Digite o número da sua opção desejada"))
    #aqui começa lógica

    if opc_user == 1: 
        print("Temos coca, fanta e guaraná")

    elif opc_user == 2:
    print("Temos coxinha, risole e empadão")

    elif opc_user == 3
    print(" temos brigadeiro, tortas e sorvete")

    else:
    print("Opção incorreta, escolha de 1 a 3")



