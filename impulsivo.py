from jogador import Jogador

class Impulsivo(Jogador):

    def __init__(self, name):
        return  super().__init__(name)

    def acao(self, propriedade):
        if not super(Impulsivo, self).acao(propriedade):
            propriedade.compra(self)


