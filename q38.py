idade = int(input("idade em dias:"))
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30
a = (anos)
b = (meses)
c = (dias)
print(a, "anos", b, "meses", c, "dias")