'''Leia uma sequência de 1000 inteiros.

Leia outro inteiro N, e seu programa deve imprimir quantas vezes o inteiro N aparece nos 1000 anteriores.

O programa para quando o primeiro inteiro dos 1000 for igual a -1.'''
while True:
    contador = 0
    lista = ""
    for i in range(999):
        n1000 = int(input())

        if n1000 == -1:
            break

        else:
            lista += f'{n1000} '

    n = input()
    contador += lista.count(n)
    print(f'{n} appeared {contador} times')


