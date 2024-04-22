idade= int(input("qual a sua idade? "))
mes= int(input("em que mês vocês nasceu? "))

if mes<=4:
    ano = 2024 - idade
else:
    ano = 2023 - idade
print(f"você nasceu em {ano}")