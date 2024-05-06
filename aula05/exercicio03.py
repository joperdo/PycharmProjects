A=[0,0,0,0,0,0,0,0,0,0]
M=[0,0,0,0,0,0,0,0,0,0]

for i in range (10):
    A[i]= int(input("digite um número: "))

X= float(input("digite mais um número: "))

for y in range (10):
    M[y]=A[y]*X

print(M)