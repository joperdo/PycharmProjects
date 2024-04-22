numero= int(input("digite um número inteiro: "))
conta= numero%2

if numero==0:
    print(f"{numero} é nulo")
elif conta==0:
    print(f"{numero} número é par")
else:
    print(f"{numero} número é impar")