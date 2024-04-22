entre= 0
fora= 0

for x in range(10):
    num = int(input("digite um número: "))
    if num>=10 and num<=20:
        entre+= 1
fora= 10-entre
print(f"você tem {entre} números entre 10 e 20 e {fora} fora desse intervalo")