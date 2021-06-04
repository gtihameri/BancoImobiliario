from jogador import Jogador
from propriedade import Propriedade

jogador = Jogador("Carlos")
outro_jogador = Jogador("Antonio")

p1_sem_dono = Propriedade(260, 60, "Casa - Paraiso")
def test_nao_aluga():
    saldo_anterior = jogador.saldo
    jogador.acao(p1_sem_dono)
    assert jogador.saldo == saldo_anterior


p2_com_dono = Propriedade(260, 60, "Casa - Paraiso")
p2_com_dono.dono = outro_jogador
def test_aluga():
    saldo_anterior = jogador.saldo
    saldo_anterior_outro = outro_jogador.saldo
    jogador.acao(p2_com_dono)
    assert jogador.saldo == saldo_anterior - p2_com_dono.aluguel and \
           outro_jogador.saldo == saldo_anterior_outro + p2_com_dono.aluguel

