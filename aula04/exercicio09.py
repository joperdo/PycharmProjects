senhaC= "quimera222"
senhaT= input("digite sua senha: ")

tentativas= 1
while senhaT != senhaC:
    tentativas += 1
    senhaT = input("senha inválida, digite de novo: ")
    if tentativas == 3 and senhaT != senhaC:
        print("senha bloqueada")
        break

if senhaT == senhaC:
    print("acesso liberado")
