nota1= float(input("digite sua 1º nota: "))
nota2= float(input("digite sua 2º nota: "))
nota3= float(input("digite sua 3º nota: "))
media= (nota1+nota2+nota3)/3

if media>=7:
    print(f"você foi aprovado com média: {media}")
elif 7>media>4:
    print(f"você vai para recuperação com média: {media}")
else:
    print(f"você foi reprovado com média: {media}")

