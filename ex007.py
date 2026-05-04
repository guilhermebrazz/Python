def diasAteInicioDoMes(mes):
    if mes == 1 :
        return 0
    elif mes == 2 :
        return 31
    elif mes == 3 :
        return 59
    elif mes == 4 :
        return 90
    elif mes == 5 :
        return 120 
    elif mes == 6 :
        return 151
    elif mes == 7 :
        return 181
    elif mes == 8 :
        return 212
    elif mes == 9 :
        return 243
    elif mes == 10 :
        return 273
    elif mes == 11 :
        return 304
    else : # mes == 12 
        return 334
    
def bissexto(ano):
    return ano % 4 == 0 or (ano % 100 == 0 and ano % 400 == 0)


dia = int(input())
mes = int(input())
ano = int(input())
dia_atual = diasAteInicioDoMes(mes) + dia
if bissexto(ano + 1):
    if mes == 6 and dia == 24:
        print("Viva Sao Joao")
    else:
        if dia_atual < 175 :
            dias_para_sao_joao = 176 - dia_atual
        else:
            dias_para_sao_joao = 176 + (365 - dia_atual)
        print(f"Faltam {dias_para_sao_joao} dias para o Sao Joao chegar")

else:
    if mes == 6 and dia == 24:
        print("Viva Sao Joao")
    else:
        if dia_atual < 175 :
            dias_para_sao_joao = 175 - dia_atual
        else:
            dias_para_sao_joao = 175 + (365 - dia_atual)
        print(f"Faltam {dias_para_sao_joao} dias para o Sao Joao chegar")
    
    