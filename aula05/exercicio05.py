nomes=["","","","",""]
senhas=["","","","",""]
menu=0

while menu!=3
    menu= int(input("digite o número de acordo com o que você queer: \n"
                    "[1]cadastro \n"
                    "[2]login \n"
                    "[3]sair"))

    if menu == 1:
        for x in range(5):
            nomes[x]=input("digite seu nome: ")
            senhas[x] = input("digite sua senha: ")

    elif menu == 2:
        nomeLogin=input("digite seu nome: ")
        senhaLogin = input("digite sua senha: ")

