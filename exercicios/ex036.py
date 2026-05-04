total = 0 
casas = 0

while True:
    carros = int(input())

    if carros == 999:
        break

    if carros > 2:
        casas += 1
        carros -= 2
        multa = carros * 12.89
        total += multa

print(total)
print(casas)