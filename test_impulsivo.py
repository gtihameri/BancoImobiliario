from impulsivo import Impulsivo
from propriedade import Propriedade




impulsivo = Impulsivo("Joao")

propriedade = Propriedade(260, 60, "Casa - Paraiso")
def test_compra():
    saldo_anterior = impulsivo.saldo
    impulsivo.acao(propriedade)
    assert impulsivo.saldo == saldo_anterior - propriedade.venda