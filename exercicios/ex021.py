n = int(input())
i = 0
for i in range(1, n+1):
    valor1 = i
    valor2 = valor1 * i
    valor3 = valor2 * i
    print(f'{valor1} {valor2} {valor3}')
    valor2 += 1
    valor3 += 1
    print(f'{valor1} {valor2} {valor3}')