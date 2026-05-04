cadastro = {}

for i in range (100):
    nome = input()

    if nome == "SAIR":
        break

    senha = int(input())
    situacao_mensalidade = input()
    cadastro[senha] = (nome, situacao_mensalidade)


while senha != -1:
    senha = int(input())

    if senha in cadastro:
        nome, situacao_mensalidade = cadastro[senha]

        if situacao_mensalidade == "P":
            print(f'{nome}, seja bem-vindo(a)!')
            
        else:
            print(f'Não está esquecendo de algo, {nome}? Procure a recepção!')
    elif senha not in cadastro and senha != -1:
        print('Seja bem-vindo(a)! Procure a recepção!')



    


