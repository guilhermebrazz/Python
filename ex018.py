'''Descrição
Escreva um programa que lê um inteiro N (1 <N <1000). Este N é o número de linhas de saída impressos por este programa.

Formato de entrada

O arquivo de entrada contém um número inteiro N.
Formato de saída'''
n = int(input())
for i in range(1, n+1): 
    valor1 = i ** 1
    valor2 = i ** 2
    valor3 = i ** 3
    print(f"{valor1} {valor2} {valor3}")