inicio= int(input("que horario seu jogo começou? "))
fim= int(input("que horario seu jogo terminou? "))

if inicio <= fim:
    duracao= fim-inicio
else:
    duracao=24-inicio+fim
print(f"seu jogo durou {duracao} horas")