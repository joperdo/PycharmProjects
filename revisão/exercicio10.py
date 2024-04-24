eleitores = int(input("digite o número de eleitores: "))
brancos=int(input("digite o número de votos brancos: "))
nulos=int(input("digite o número de votos nulos: "))
validos=int(input("digite o número de votos validos: "))

while (brancos+nulos+validos) != eleitores:
      validos = int(input("digite o número de votos validos de novo: "))

porcentB = 100 * (brancos/eleitores)
porcentN = 100 * (nulos/eleitores)
porcentV = 100 * (validos/eleitores)

print(f"o percentual que cada um representa: \n"
      f"votos brancos: {porcentB}%; \n"
      f"votos nulos: {porcentN}%; \n"
      f"votos validos: {porcentV}%.")