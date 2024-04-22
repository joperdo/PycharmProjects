anos= int(input("em que ano você nasceu? "))
meses= int(input("em que mês você nasceu? "))
dias= int(input("em dia você nasceu? "))

canos=365*anos
cmeses=30*meses
conta= canos+cmeses+dias

print(f"você tem {conta} dias de vida")