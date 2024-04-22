alunos = int(input("quantos alunos tem na sua sala? "))

j= 0
soma= 0
while j < alunos:
    num = int(input("digite sua nota: "))
    soma = soma + num
    j= j + 1

mediaA= soma/alunos

print(mediaA)