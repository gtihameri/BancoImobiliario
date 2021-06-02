
class Jogador:

    def __init__(self, nome):

        self.nome = nome
        self.posicao = 0
        self.saldo = 300
        self.jogando = True

    def acao(self, propriedade):
        if propriedade.temdono() and propriedade.dono != self:
            propriedade.aluga(self)
            return True
        else:
            return False




