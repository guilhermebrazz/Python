'''Faça um programa para retornar a quantidade de dias de um mês dado. Se o mês for fevereiro, deve-se verificar se o ano é bissexto e retornar a quantidade de dias correta.'''
def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
mes = int(input())
ano = int(input())
if mes == 2:
    if bissexto(ano):
        print(29)
    else:
        print(28)

if mes in [4, 6, 9, 11]:
    print(30)
elif mes in [1, 3, 5, 7, 8, 10, 12]: 
    print(31)