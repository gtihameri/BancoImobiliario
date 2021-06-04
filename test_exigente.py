from exigente import Exigente
from propriedade import Propriedade




exigente = Exigente("Jpse")

p1_aluguel_60 = Propriedade(260, 60, "Casa - Paraiso")
def test_compra_atende_criterio():
    saldo_anterior = exigente.saldo
    exigente.acao(p1_aluguel_60)
    assert exigente.saldo == saldo_anterior - p1_aluguel_60.venda

p2_aluguel_5 = Propriedade(60, 5, "Apartamento - Ibirapuera")
def test_nao_compra_nao_atende_criterio():
    saldo_anterior = exigente.saldo
    exigente.acao(p2_aluguel_5)
    assert  exigente.saldo == saldo_anterior