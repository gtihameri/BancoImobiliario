from propriedade import Propriedade, SEM_DONO
from jogador import Jogador



def test_sem_dono():
    # Propriedade criada sem dono
    propriedade = Propriedade(200, 30, "Loja - Vila Mariana")
    assert propriedade.temdono() == False


def test_com_dono():
    propriedade = Propriedade(200, 30, "Loja - Vila Mariana")
    jogador = Jogador("Alberto")
    propriedade.dono = jogador
    assert propriedade.temdono() == True

def test_retira_dono():
    propriedade = Propriedade(200, 30, "Loja - Vila Mariana")
    jogador = Jogador("Alberto")
    propriedade.dono = jogador
    assert propriedade.dono == jogador
    propriedade.retira_dono()
    assert propriedade.dono == SEM_DONO

def test_compra():
    propriedade = Propriedade(200, 30, "Loja - Vila Mariana")
    jogador = Jogador("Alberto")
    saldo_anterior = jogador.saldo
    propriedade.compra(jogador)
    assert jogador.saldo == saldo_anterior - propriedade.venda


def test_aluga():
    propriedade = Propriedade(200, 30, "Loja - Vila Mariana")
    jogador = Jogador("Alberto")
    saldo_anterior = jogador.saldo
    propriedade.aluga(jogador)
    assert jogador.saldo == saldo_anterior - propriedade.aluguel

