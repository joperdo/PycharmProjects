notas=[0,0,0,0,0]
soma=0
cont=0

for x in range (5):
    notas[x]= float(input("digite uma nota: "))

for y in range (5):
    soma+=notas[y]
media=soma/5

for z in range (5):
    if notas[z] >= media:
        cont+=1

print(f"a média da sala foi {media} e {cont} alunos foram aprovados")