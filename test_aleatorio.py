from jogador import Jogador
from aleatorio import Aleatorio
from propriedade import Propriedade

propriedade = Propriedade(60, 5, "Apartamento - Ibirapuera")
aleatorio = Aleatorio("Maria")

def test_compra_propriedade():
    saldo_anterior = aleatorio.saldo
    aleatorio.acao(propriedade)
    assert  aleatorio.saldo == saldo_anterior  or \
            aleatorio.saldo == saldo_anterior - propriedade.venda or \
            aleatorio.saldo == saldo_anterior - propriedade.aluguel
jogador = Jogador("Carlos")
propriedade.dono = jogador

def test_aluga_propriedade():
    saldo_anteriro = aleatorio.saldo
    aleatorio.acao(propriedade)
    assert aleatorio.saldo == saldo_anteriro - propriedade.aluguel
