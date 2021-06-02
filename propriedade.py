from jogador import Jogador

from colorama import Fore

SEM_DONO = Jogador(None)
DEBUG = False


class Propriedade:

    def __init__(self, venda, aluguel, descricao):
        self.venda, self.aluguel, self.descricao = venda, aluguel, descricao
        self.dono = SEM_DONO

    def temdono(self):
        """Retorna se a propriedade tem dono"""
        if self.dono != SEM_DONO:
            return True
        else:
            return False

    def retira_dono(self):
        self.dono = SEM_DONO

    def imprime_compra(self, jogador):
        if DEBUG:
            print(
                f"** Jogador - {jogador.nome}({jogador.__class__.__name__}) na posicao {jogador.posicao} {Fore.GREEN} compra  {Fore.RESET} {self.descricao} - Saldo:{jogador.saldo} ")

    def imprime_aluga(self, jogador, outro_jogador):
        if DEBUG:
            print(
                f"** Jogador - {jogador.nome}({jogador.__class__.__name__}) na posicao {jogador.posicao} {Fore.BLUE}  aluga   {Fore.RESET}{self.descricao} de {outro_jogador.nome} - Saldo:{jogador.saldo}")

    def compra(self, jogador):
        """Compra de uma propriedade por um jogador"""
        if jogador.saldo > self.venda:
            jogador.saldo -= self.venda
            self.dono = jogador
        self.imprime_compra(jogador)

    def aluga(self, jogador):
        """Jogador aluga propriedade e paga ao proprietario"""
        jogador.saldo -= self.aluguel
        (self.dono).saldo += self.aluguel
        self.imprime_aluga(jogador, self.dono)
        if jogador.saldo < 0:
            jogador.jogando = False
