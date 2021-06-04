from tabuleiro import Tabuleiro
from jogador import Jogador
from propriedade import Propriedade, SEM_DONO

tabuleiro = Tabuleiro()

def test_proxima_posicao():
    POS = 4
    tabuleiro = Tabuleiro()
    # Testa se a proxima posiçao fica de 1 a 6 casas a frente
    jogador = Jogador("Manuel")
    jogador.posicao = POS
    proxima_posicao = tabuleiro.proxima_posicao(jogador)
    assert  proxima_posicao >=  POS + 1 and \
            proxima_posicao <=  POS + 6

def test_proxima_posicao_ultima_casa():
    POS = 20
    tabuleiro = Tabuleiro()
    # Testa se a proxima posiçao fica de 1 a 6 casas a frente
    jogador = Jogador("Manuel")
    jogador.posicao = POS
    proxima_posicao = tabuleiro.proxima_posicao(jogador)
    assert proxima_posicao >=  1 and \
           proxima_posicao <=  6

def test_perde_propriedade():
    jogador1 = Jogador("Manuel")
    jogador2 = Jogador("Antonio")

    for i in range(0,len(tabuleiro.propriedades)-1, 2):
        tabuleiro.propriedades[ i ].dono = jogador1
        tabuleiro.propriedades[i+1].dono = jogador2

    tabuleiro.perde_propriedades(jogador1)

    assert len([p for p in tabuleiro.propriedades if p.dono == jogador1]) == 0
