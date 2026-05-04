'''Rafinha sabe que em sua cidade o valor da KWh de energia varia da forma mostrada abaixo.

Até 99 KWh: R$1.35
100 até 299 KWh: R$1.55
300 até 574 KWh: R$1.75
Maior ou igual a 575 KWh: R$2.15
Ele também sabe que quando o consumo é maior que 300KWh é cobrado uma taxa de 10% no valor da conta e o preço mínimo de qualquer conta é R$35. Escreva um programa para auxiliar Rafinha a visualizar o valor de sua conta elétrica e qual o valor do KWh aplicado em sua conta.
OBS: O formato da saída deve ser feito com duas casas decimais.'''
kwh = int(input())
energia = 0
conta = 0
if kwh <= 99:
    energia = 1.35
elif (kwh >= 100) and (kwh <= 299):
    energia = 1.55
elif (kwh >= 300) and (kwh <= 574):
    energia = 1.75 
else:
    energia = 2.15
if kwh >= 35:
    if kwh < 300:
        conta = energia * kwh
    else:
        conta = energia * kwh
        conta += conta * 0.1
else:
    conta = 35

print(f'{conta:.2f}')
print(f'{energia:.2f}')
