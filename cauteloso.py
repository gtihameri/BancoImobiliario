from jogador import Jogador

RESERVA = 80
class Cauteloso(Jogador):

    def __init__(self, name):
        return  super().__init__(name)

    def acao(self, propriedade):
        if not super(Cauteloso, self).acao(propriedade):
            # Se atende o criterio do cauteloso
            if self.saldo - propriedade.venda > RESERVA:
                propriedade.compra(self)