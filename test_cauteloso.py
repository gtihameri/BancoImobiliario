from cauteloso import Cauteloso
from propriedade import Propriedade

propriedade = Propriedade(60, 5, "Apartamento - Ibirapuera")
cauteloso = Cauteloso("Ana")
cauteloso.saldo = 180

def test_compra_tem_reserva():
    saldo_anterior = cauteloso.saldo
    cauteloso.acao(propriedade)
    assert cauteloso.saldo == saldo_anterior - propriedade.venda

def test_nao_compra_nao_tem_reserva():
    saldo_anterior = cauteloso.saldo
    cauteloso.acao(propriedade)
    assert  cauteloso.saldo == saldo_anterior