nota1= float(input("nota 1: "))

while nota1 >10 or nota1 <0:
     nota1= float(input("digite uma nota entre 0 e 10: "))

nota2= float(input("nota 2: "))

while nota2 >10 or nota2 <0:
     nota2= float(input("digite uma nota entre 0 e 10: "))

media= (nota1+nota2)/2
print(f"sua média é {media}")

resposta= input("deseja realizar um novo calculo? ")
restosta= "sim"
while resposta == "sim" or resposta == "Sim":
    nota1 = float(input("nota 1: "))

    while nota1 > 10 or nota1 < 0:
        nota1 = float(input("digite uma nota entre 0 e 10: "))

    nota2 = float(input("nota 2: "))

    while nota2 > 10 or nota2 < 0:
        nota2 = float(input("digite uma nota entre 0 e 10: "))

    media = (nota1 + nota2) / 2
    print(f"sua média é {media}")
    resposta = input("deseja realizar um novo calculo? ")
