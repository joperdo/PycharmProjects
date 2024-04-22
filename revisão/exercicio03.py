idade= int(input("qual a sua idade? "))
mes= int(input("em que mês vocês nasceu? "))
anoAtual= 2024
mesAtual=4

if mes<=mesAtual:
    ano = anoAtual - idade
else:
    ano = anoAtual -1 - idade
print(f"você nasceu em {ano}")