from jogador import Jogador
ALUGUEL_MINIMO = 50
class Exigente(Jogador):

    def __init__(self, name):
        return  super().__init__(name)

    def acao(self, propriedade):
        if not super(Exigente, self).acao(propriedade):
            # Se atende os criterios do exigente
            if propriedade.aluguel > ALUGUEL_MINIMO:
                propriedade.compra(self)