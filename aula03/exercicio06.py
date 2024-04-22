#digite 10 numeros e some apenas os ímpares

soma=0
for impa in range(1, 11):
    numero = int(input("digite um número: "))
    if numero % 2 != 0:
        soma = soma + numero
print(impa)