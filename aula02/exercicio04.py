c= input("qual o tipo de combustível? \n"
         "'e' para estanol e 'g' para gasolina: ")
l= float(input("litros: "))
contae= l*4.9
contag= l*5.8

if c=="e" or c=="E":
    print(f"preço: {contae}")
elif c=="g" or c=="G":
    print(f"preço: {contag}")
else:
    print("tipo de combustível invalido")