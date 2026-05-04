'''Descrição 

Por isso, a SBC decidiu fiscalizar com mais rigor o uso de seus elevadores: foi instalado um sensor em cada porta que detecta a quantidade de pessoas que saem e entram em cada andar do elevador. A SBC tem os registros do sensor de todo um dia de funcionamento do elevador (que sempre começa vazio). 

Eles sabem que as pessoas são educadas e sempre deixam todos os passageiros que irão sair em um andar saírem antes de outros passageiros entrarem no elevador, mas ainda assim eles têm tido dificuldade em decidir se a capacidade máxima do elevador foi excedida ou não.

Escreva um programa que, dada uma sequência de leituras do sensor e a capacidade máxima do elevador, determina se a capacidade máxima do elevador foi excedida em algum momento. 
 
Formato de entrada

A primeira linha da entrada contém dois inteiros N e C, indicando o número de leituras realizadas pelo sensor e a capacidade máxima do elevador, respectivamente (1 <= N <= 1000 e 1 <= C <= 1000). As N linhas seguintes contêm, cada uma, uma leitura do sensor. Cada uma dessas linhas contém dois inteiros S e E, indicando quantas pessoas saíram e quantas pessoas entraram naquele andar, respectivamente (0 <= S <= 1000 e 0 <= E <= 1000).'''
num_leituras, cap_elevador = map(int, input().split())
pessoas = 0
excedeu = False
for i in range(num_leituras):
    sairam, entraram = map(int, input().split())

    pessoas -= sairam
    pessoas += entraram

    if pessoas > cap_elevador:
        excedeu = True

if excedeu:
    print('S')
else:
    print('N')
