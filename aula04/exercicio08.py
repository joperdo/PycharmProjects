num1 = float(input("digite um número: "))
num2 = float(input("digite outro número: "))

while num2 == 0:
    num2 = int(input("digite um número válido: "))

divisao= num1/num2
print(f"a divisão dos seus números é {divisao}")