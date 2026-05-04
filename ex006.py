'''A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.'''
entrada = input()
valores = entrada.split
qnt_dias = int(valores[0])
kms_total = int(valores[1])
conta_dias = 90 * qnt_dias
kms_taxa = kms_total - 100
if kms_taxa <= 0:
    kms_taxa = 0
else:
    conta_kms = kms_taxa * 12

total = conta_dias + conta_kms
print(f'{total:.2f}')