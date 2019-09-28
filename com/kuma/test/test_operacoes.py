import pytest
from com.kuma.calcula_parcela import valor_pagamento
from com.kuma.contaCorrente import ContaCorrente
from com.kuma.convertehora import convertehora


def test_deposito():
    '''
    teste
    '''
    contacorrente = ContaCorrente(1222, "pablo")
    contacorrente.deposito(100)
    assert contacorrente.saldo == 100, "Valor e 100"


def test_alterarnome():
    '''
    teste
    '''
    contacorrente = ContaCorrente(1222, "pablo")
    contacorrente.alterarnome("julio")
    assert contacorrente.nomecorrentista == "julio", " Era Pablo"


def test_saque():
    '''
    teste
    '''
    contacorrente = ContaCorrente(1222, "pablo")
    contacorrente.saque(100)
    assert contacorrente.saldo == -100, "Valor e 100"


def test_retornarnone():
    '''
    teste
    '''
    operacao = convertehora(24, 0)
    assert operacao == None, "Deveria ser None"


def test_retornarmeiodia():
    '''
    teste
    '''
    operacao = convertehora(0, 10)
    assert operacao == "12:10 AM", "Deveria ser 12:10 AM"


def test_retornaronze():
    '''
    teste
    '''
    operacao = convertehora(9, 10)
    assert operacao == "09:10 AM", "Deveria ser 9:10 AM"


def test_doisdiasatraso():
    '''
    teste
    '''
    operacao = valor_pagamento(100, 2)
    assert operacao == 105, "Deveria ser 105"


def test_valorzero():
    operacao = valor_pagamento(-1, 0)
    assert operacao == None, "Deveria ser 0"


def test_sematraso():
    '''
    teste
    '''
    operacao = valor_pagamento(100, 0)
    assert operacao == 100, "Deveria ser 100"
