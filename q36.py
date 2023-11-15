valor = int(input("valor:"))
notas100 = notas50 = notas20 = notas10 = nota5 = nota2= nota1= 0
while valor != 0:
    if valor >=100:
        notas100 += 1
        valor -=100
    elif valor >=50:
        notas50 += 1
        valor -=50
    elif valor >=20:
        notas20 += 1
        valor -=20
    elif valor >=10:
        notas10 += 1
        valor -=10
    elif valor >=5:
        nota5 += 1
        valor -=5
    elif valor >=2:
        nota2 += 1
        valor -=2
    elif valor >=1:
        nota1 += 1
        valor -=1
    else:
        nota1 += 1
        valor -= 1
print("O valor foi:", valor)
print("Notas de 100:", notas100)
print("Notas de 50:", notas50)
print("Notas de 20:", notas20)
print("Notas de 10:", notas10)
print("Notas de 5", nota5)
print("Notas de 2:", nota2)
print("Notas de 1:", nota1)