def valor_pagamento(valor, dias_atraso):
    '''
    teste
    '''
    if valor < 0:
        return None
    if dias_atraso > 0:
        multa = valor * 0.03
        adicional_atraso = valor * (dias_atraso * 0.01)
        return valor + multa + adicional_atraso
    else:
        return valor


'''
# Entrada de Dados
valor = 1
while (valor != 0):
    valor = float(raw_input('Informe o valor da prestacao: '))
    if (valor != 0):
        diasAtraso = int(raw_input('Informe a quantidade de dias de atraso: '))
        print ("Valor a ser pago: %.2f" % valorPagamento(valor, diasAtraso))
'''
