'''Poliana resolveu economizar dinheiro para comprar um carro.

Ela traçou como meta depositar um valor X em seu cofrinho no primeiro dia da semana, e ir guardando a cada manhã o valor do dia anterior acrescido de pelo menos R$ 0,50. Mas será que ela vai conseguir fazer isso todos os dias?

Para saber se o plano de Poliana vai dar certo, escreva um programa que receba como entrada o valor inicial depositado, e em seguida os valores depositados a cada dia. Ao final, exiba o total poupado e quantas vezes Poliana conseguiu cumprir sua meta.

Dica: é preciso sempre comparar o valor do dia com o do dia anterior

Formato de entrada

Valores reais, um para cada dia da semana'''

val_inicial = float(input())
temp = val_inicial
soma = val_inicial
c = 0

for i in range(6):
    val_dia = float(input())
    soma += val_dia
    
    if val_dia >= temp + 0.50:
        c += 1
    
    temp = val_dia

print(f'R$ {soma:.2f}')
print(c)


