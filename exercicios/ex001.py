'''Faça um programa que receba a quantidade de m3 de água consumidos e o custo por litro de água e calcule:

a) O valor a ser pago pela água; 

b) O valor a ser pago pelo esgoto, sabendo que este corresponde a 80% do valor da água consumida;

c) O valor total da conta, considerando água e esgoto.

Dica: Lembre-se que 1 m3 = 1.000 litros
entrada: 5.0 0.1'''
entrada = input()
valores = entrada.split()
metro3 = float(valores[0])
val_litro = float(valores[1])
tot_litros = metro3 * 100
val_agua = tot_litros * val_litro
esgoto = val_agua * 0.80
total = val_agua + esgoto
print (f'{val_agua:.2f}')
print (f'{esgoto:.2f}')
print (f'{total:.2f}')