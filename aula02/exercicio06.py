hora1= int(input("1º horas: "))
min1= int(input("1º minutos: "))
hora2= int(input("2º horas: "))
min2= int(input("2º minutos: "))

if hora1>12:
    hora1= hora1-12
if hora2>12:
    hora2= hora2-12
hora = hora1 + hora2

min= min1+min2
sobramin= (min1+min2)%60
sobrahora= (min1+min2)//60

if min>=60:
    hora= hora+sobrahora
    min= sobramin

if hora > 12:
    hora = hora - 12

print(f"a soma dos horarios foi {hora}:{min}")
