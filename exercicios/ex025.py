def primo(n):
    contador = 0

    for i in range(1, n + 1):

        if n % i == 0:
            contador += 1

    return contador == 2

x = int(input())
y = int(input())
s = x + y

if not primo(x):
    print(f'O numero {x} nao eh primo')

elif not primo(y):
    print(f'O numero {y} nao eh primo')
    
elif primo(x) and primo(y) and not primo(s):
    print(f'A soma de {x} e {y} nao eh um primo')

elif primo(x) and primo(y) and primo(s):
    print(f'A soma de {x} e {y} eh um primo')
        