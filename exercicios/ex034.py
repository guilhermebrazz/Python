def tamanhociclo(n):
    lista = f'{n} '

    while n != 1:

        n = n//2 if n % 2 == 0 else 3*n + 1
        lista += f'{n} '

    resultado = len(lista.split())

    return resultado
while True:
    try:
        n, lim = map(int, input().split())
        maior = 0
    except EOFError:
        break
    if n < lim:
        for i in range(n, lim + 1):
            aux = tamanhociclo(i)

            if aux > maior:
                maior = aux
    else:
        for i in range(lim, n + 1):
            aux = tamanhociclo(i)

            if aux > maior:
                maior = aux
    print(f'{n} {lim} {maior}')
        