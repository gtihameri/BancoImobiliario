from jogador import Jogador
import random

PROBABILIDADE_DE_COMPRA = 0.5
class Aleatorio(Jogador):

    def __init__(self, name):
        return  super().__init__(name)

    def acao(self, propriedade):
        """Acao a ser executada quando o jogador engra na propriedade"""
        if not super(Aleatorio, self).acao(propriedade):
            # Se atende criterio aleatorio
            if random.random() > PROBABILIDADE_DE_COMPRA:
                propriedade.compra(self)
