duracaosegundos = int(input("Digite o tempo de duração em segundos do evento na fábrica: "))
horas = duracaosegundos // 3600
minutos = (duracaosegundos % 3600) // 60
segundos = duracaosegundos % 60
print(horas, ":", minutos, ":", segundos )