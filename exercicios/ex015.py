''' Ache a soma de todos números naturais múltiplos de 3 ou 5 menores que n.

Formato de entrada

Um número inteiro n.

Formato de saída

 A soma de todos os números naturais múltiplos de 3 e 5 menores que n, com uma quebra de linha.

Exemplos de:'''
c = 0
n = int(input())
for i in range(n):
    if (i % 3 == 0) or (i % 5 == 0):
        c += i
print(c)