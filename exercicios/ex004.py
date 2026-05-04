'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias. entrada: 576'''
total = int(input())
not100 = total // 100
resto = total % 100

not50 = resto // 50
resto = resto % 50

not20 = resto // 20
resto = resto % 20

not10 = resto // 10
resto = resto % 10

not5 = resto // 5
resto = resto % 5

not2 = resto // 2
resto = resto % 2

not1 = resto // 1
resto = resto % 1
print (total)
print (f'{not100} nota(s) de R$ 100,00')
print (f'{not50} nota(s) de R$ 50,00')
print (f'{not20} nota(s) de R$ 20,00')
print (f'{not10} nota(s) de R$ 10,00')
print (f'{not5} nota(s) de R$ 5,00')
print (f'{not2} nota(s) de R$ 2,00')
print (f'{not1} nota(s) de R$ 1,00')