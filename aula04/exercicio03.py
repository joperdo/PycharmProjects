negativo= 0

for x in range(10):
    num = int(input("digite um número: "))
    if num<0:
        negativo+= 1

print(f"você tem {negativo} números negativos")