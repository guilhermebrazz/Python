'''Descrição
Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.

Obs: o intervalo pode ser crescente ou decrescente

Formato de entrada

Dois números inteiros

Dica: os números podem ser informados em qualquer ordem (não necessariamente o primeiro será menor que o segundo)'''
a = int(input())
b = int(input())
soma = 0 
if a < b:
    for i in range(a, b + 1):
        if i > 0:
            soma += i
elif a == b:
    soma = a
else:
    for i in range(b, a + 1):
        if i > 0:
            soma += i
print(soma)
