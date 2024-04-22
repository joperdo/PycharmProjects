soma=0
for x in range (2):
    nota= float(input("digite uma nota: "))
    soma= soma + nota
media= soma/2

if media>=4 and media<=7:
    print("você está de recuperação")
elif media<4:
    print("você reprovou")
else:
    print("você está aprovado")
