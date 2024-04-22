perg = "sim"
while perg== "sim":
    num = int(input("digite um número: "))
    while num == 0:
        num = int(input("digite um número válido: "))
    if num > 0:
        print("seu número é positivo")
    elif num < 0:
        print("seu número é negativo")
    perg = input("queer fazer de novo? ")
