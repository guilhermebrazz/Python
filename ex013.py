'''Escreva um programa que calcule os N termos da série S  abaixo:

 S = (1/3) + (2/6) + (3/9) + (4/12) + …

O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais.
ENTRADA:
Um valor N que representa a quantidade de termos da série.
'''

qnt = int(input())
i = 0 
d = 0
soma = 0
mes = ''
if qnt == 0:
        print(f'{qnt:.2f}')
else:
    while i < qnt: 
        i += 1
        if i != qnt:
            d = i * 3
            mes += f'({i}/{d}) + '
        else:
            d = i * 3
            mes += f'({i}/{d})'
        d = i * 3
        soma += i / d
    print(mes)
    print(f'{soma:.2f}')