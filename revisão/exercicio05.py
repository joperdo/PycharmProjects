duvida= "sim"
while duvida== "sim":
    num= int(input("digite um número: "))

    if num % 2 ==0:
        print(f"{num} é um número par")
    else:
        print(f"{num} é um número impar")
    duvida= input("quer fazer de novo? ")
