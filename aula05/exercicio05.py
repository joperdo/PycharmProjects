nomes=["","","","",""]
senhas=["","","","",""]

for x in range (5):
    nomes[x]= input("digite seu nome: ")
    senhas[x] = input("digite sua senha: ")

for z in range (5):
    print(f"login: {nomes[z]} \n"
          f"senha: {senhas[z]} \n"
          f"posição: {z}")