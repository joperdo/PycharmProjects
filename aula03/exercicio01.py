mes= int(input("digite o mês do seu aniversário em número: "))

if mes<=12 and mes>0:
    if mes== 1:
        print("você faz aniversário em janeiro")
    elif mes == 2:
        print("você faz aniversário em fevereiro")
    elif mes == 3:
        print("você faz aniversário em março")
    elif mes == 4:
        print("você faz aniversário em abril")
    elif mes == 5:
        print("você faz aniversário em maio")
    elif mes == 6:
        print("você faz aniversário em junho")
    elif mes == 7:
        print("você faz aniversário em julho")
    elif mes == 8:
        print("você faz aniversário em agosto")
    elif mes == 9:
        print("você faz aniversário em setembro")
    elif mes == 10:
        print("você faz aniversário em outubro")
    elif mes == 11:
        print("você faz aniversário em novembro")
    elif mes == 12:
        print("você faz aniversário em dezembro")
else:
    print("esse mês não existe")