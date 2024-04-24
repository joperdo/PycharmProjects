pergunta=0
while pergunta!=3:
    pergunta=float(input(f"qual você quer calcularr? trângulo(1), quadrado(2), nenhum(3): "))
    if pergunta==1:
        baseT = float(input("qual a base do seu triângulo? "))
        AlturaT = float(input("qual a altura do seu triângulo? "))
        AT = (baseT * AlturaT) / 2
        print(f"a área do seu triângulo é {AT}")
    elif pergunta==2:
        baseQ = float(input("qual a base do seu triângulo? "))
        AlturaQ = float(input("qual a altura do seu triângulo? "))
        AQ = baseQ * AlturaQ
        print(f"a área do seu quadrado é {AQ}")
    else:
        print("digite um número válido")

