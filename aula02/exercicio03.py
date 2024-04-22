nome1= input("digite o nome do 1º time: ")
g1= int(input("digite o número de gols desse time: "))
nome2= input("digite o nome do 2º time: ")
g2= int(input("digite o número de gols desse time: "))

if g1!=g2:
    if g1>g2:
        print(f"{nome1} é venceu!")
    else:
        print(f"{nome2} é venceu!")
else:
    print("empate.")