from propriedade import Propriedade
from impulsivo import Impulsivo
from aleatorio import Aleatorio
from exigente import Exigente
from cauteloso import Cauteloso
import random
import time
from colorama import Fore

CONTINUA_JOGO = True
DADO = [1,2,3,4,5,6]
LIMITE = 1000
DEBUG = False

class Tabuleiro:

    def __init__(self):
        self.rodada = 0
        self.vencedor = "Ninguem"
        self.timeout = False
        self.propriedades = [
            Propriedade(0,0,"Inicio"),                              #0 Inicio
            Propriedade(60,  5, "Apartamento - Ibirapuera"),        #1
            Propriedade(60, 35, "Loja - Moema"),                    #2
            Propriedade(20, 5, "Supermercado - Brooklin"),          #3
            Propriedade(70, 15, "Apartamento - Santo Amaro"),       #4
            Propriedade(120, 55, "Mercearia - Socorro"),            #5
            Propriedade(90, 60, "Pastelaria - Tatuape"),            #6
            Propriedade(60, 15, "Loja - Penha"),                    #7
            Propriedade(30,  5, "Farmacia - Santana"),              #8
            Propriedade(230, 60, "Hotel - Casa Verde"),             #9
            Propriedade(40,  5, "Escola - Butantã"),                #10
            Propriedade(110, 55, "Apartamento - Pirituba"),         #11
            Propriedade(60 , 15, "Loja - Freguesia do O"),          #12
            Propriedade(50, 15, "Supermercado - Lapa"),             #13
            Propriedade(130, 50, "Apartamento - Pinheiros"),        #14
            Propriedade(60, 5 , "Mercearia - Pompeia"),             #15
            Propriedade(30, 5, "Hotel - Vila Madalena"),            #16
            Propriedade(85, 30, "Loja - Santa Ifigenia"),           #17
            Propriedade(70 , 25, "Farmacia - Anhangabau"),          #18
            Propriedade(60, 10, "Minimercado - Liberdade"),         #19
            Propriedade(20,  5, "Escola - Mooca"),                  #20
        ]

        self.NUM_PROPRIEDADES = len(self.propriedades) - 1

        self.jogadores = [
            Impulsivo("João"),
            Exigente("José"),
            Cauteloso("Ana"),
            Aleatorio("Maria")
            ]

        self.JOGANDO = len(self.jogadores)

    def proxima_posicao(self, jogador):
            dado = random.choice(DADO)
            # se passar da ultima casa começa da primeira casa
            proxima_pos = jogador.posicao + dado
            if proxima_pos > self.NUM_PROPRIEDADES:
                # ao completar uma volta o jogador ganha 100
                jogador.saldo += 100
                return proxima_pos - self.NUM_PROPRIEDADES
            else:
                return proxima_pos

    def perde_propriedades(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.dono == jogador:
                propriedade.retira_dono()

    def exclui_jogador(self,jogador):
        jogador.jogando = False
        self.JOGANDO -= 1
        self.perde_propriedades(jogador)
        if DEBUG:
            print(f"{Fore.RED} ** Jogador {jogador.nome} excluido {Fore.RESET}")

    def acha_vencedor(self):
        maior_saldo = 0
        for jogador in self.jogadores:
            if jogador.jogando:
                if jogador.saldo > maior_saldo:
                    maior_saldo = jogador.saldo
                    self.vencedor = jogador

    def partida(self):
        random.shuffle(self.jogadores)
        while self.JOGANDO > 1:
            for jogador in self.jogadores:
                if jogador.jogando:
                    jogador.posicao = self.proxima_posicao(jogador)
                    # Decide o que o jogador vai fazer nessa propriedade
                    propriedade = self.propriedades[jogador.posicao]
                    if DEBUG:
                        print(f"Rodada {self.rodada} - Jogando {jogador.nome}, Saldo: {jogador.saldo} - Caiu na propriedade de {(propriedade.dono).nome} - Valor:{propriedade.venda}, Aluguel:{propriedade.aluguel}")
                    jogador.acao(propriedade)
                    # Exclui jogadores sem dinheiro
                    if jogador.saldo < 0:
                        self.exclui_jogador(jogador)
                    #time.sleep(0.1)
                    self.rodada += 1
                    if self.rodada > LIMITE:
                        self.rodada -= 1
                        self.timeout = True
                        self.JOGANDO = 0
                        break

        self.acha_vencedor()