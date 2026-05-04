'''Descrição

Escreva um programa que transforme o computador numa urna eletrônica para eleição, em segundo turno, para presidente de um país chamado Ambrolândia. Nessas eleições concorrem os candidatos 83-Alibabá e 93-Alcapone. Cada voto deve ser dado pelo número do candidato, permitindo-se ainda o voto 0 para voto em branco. Qualquer voto diferente dos já citados é considerado nulo. No final da eleição o programa deve emitir um relatório contendo a votação de cada candidato, a quantidade votos em branco, a quantidade de votos nulos e o candidato eleito e os respectivos percentuais.

Em Ambrolândia, o percentual de votos é calculado considerando os votos válidos. O voto nulo não é considerado um voto válido. Entretanto, o voto em branco é considerado um voto válido.

Formato de entrada


A entrada consiste de um conjunto de números inteiros, um por linha. A eleição termina quando o número digitado é -1.

O número de inteiros dados é maior que um e menor que cem milhões.

Considere também que cada candidato tem pelo menos um voto.'''
alibaba = 0
alcapone = 0
branco = 0
nulo = 0
i = 0
while i >= 0:
    i = int(input())
    if i == 83:
       alibaba += 1
    elif i == 93:
        alcapone += 1
    elif i == 0:
        branco += 1
    else:
        if i > 0:
            nulo += 1

print(alibaba)
print(alcapone)
print(branco)
print(nulo)
total = alibaba + alcapone + branco

if alibaba > alcapone:
    print(83)
else:
    print(93)
porcentagem83 = (alibaba / total) * 100
porcentagem93 = (alcapone / total) * 100
print(f'{porcentagem83:.2f}')
print(f'{porcentagem93:.2f}')