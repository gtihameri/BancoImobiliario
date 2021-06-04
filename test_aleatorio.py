from jogador import Jogador
from aleatorio import Aleatorio
from propriedade import Propriedade

propriedade = Propriedade(60, 5, "Apartamento - Ibirapuera")
aleatorio = Aleatorio("Maria")

def test_compra_propriedade():
    NUM_TENTATIVAS = 5000
    resultado = []
    for i in range(NUM_TENTATIVAS):
        propriedade = Propriedade(60, 5, "Apartamento - Ibirapuera")
        aleatorio = Aleatorio("Maria")
        saldo_anterior = aleatorio.saldo
        aleatorio.acao(propriedade)
        if aleatorio.saldo == saldo_anterior - propriedade.venda:
            # Comprou
            resultado.append("comprou")
        else:
            resultado.append(("Nao Comprou"))
        compras = len([r for r in resultado if r == "comprou"])/NUM_TENTATIVAS*100

    assert  compras > 48 and compras < 52

def test_aluga_propriedade():
    jogador = Jogador("Carlos")
    propriedade.dono = jogador
    saldo_anteriro = aleatorio.saldo
    aleatorio.acao(propriedade)
    assert aleatorio.saldo == saldo_anteriro - propriedade.aluguel
