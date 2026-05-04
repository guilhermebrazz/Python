def linhas(numero):
    resultado = ""

    for i in range (1, numero + 1):
        lista = ""

        if i == 1:
            lista += f'{i}'

        else:

            for c in range(i):
                lista += f'{i}-'
        if len(lista) > 1:
            lista = lista[:-1]
        resultado += lista + "\n"
    return resultado
n = int(input())
print(linhas(n))