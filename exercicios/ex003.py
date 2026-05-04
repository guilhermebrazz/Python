'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica e informe-o expresso no formato horas:minutos:segundos.'''
tempo = int(input())
horas = tempo // 3600
resto = tempo % 3600

minutos = resto // 60
seg = resto % 60

print (f'{horas}:{minutos}:{seg}')