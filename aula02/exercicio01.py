n1= int(input("digite um número: "))
n2= int(input("digite outro número: "))
if n1!=n2:
    if n1<n2:
        print(f"em ordem crescente: {n1}, {n2}")
    else:
        print(f"em ordem crescente: {n2}, {n1}")
else:
    print("números iguais")