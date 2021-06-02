from tabuleiro import Tabuleiro
from time import sleep

NUM_PARTIDAS = 300
partida = 1
resultados = []


def relatorio_resultados():
    num_resultados = len(resultados)
    # Partdas que terminaram em timeout
    num_timeouts = sum(r['timeout'] for r in resultados)
    # Numero medio de rodadas
    num_rodadas = sum(r['rodadas'] for r in resultados)/num_resultados
    # Calcula a porcentagem de vitorias por caracteristica
    estatisticas = {}
    for r in resultados:
        estatisticas[r['vencedor']] = 0
    for r in resultados:
        estatisticas[r['vencedor']] += 1
    for k in list(estatisticas):
        estatisticas[k] = estatisticas[k] * 100 / num_resultados
    # Mostra resultados
    print(f"Numero de timeouts : {num_timeouts}")
    print("Numero de rodadas medias : {:3.2f}".format(num_rodadas))
    print("Porcentagem por comportamento")
    for key in estatisticas.keys():
        print(" {0:10s} {1:3.2f}%".format(key,estatisticas[key]))
    print(f"O comportamento que mais vence é {max(estatisticas,key=estatisticas.get)} ")

while partida <= NUM_PARTIDAS:
    bancoimobiliario = Tabuleiro()
    bancoimobiliario.partida()
    classe_vencedor = (bancoimobiliario.vencedor).__class__.__name__
    resultados.append({'timeout': bancoimobiliario.timeout, 'rodadas': bancoimobiliario.rodada, 'vencedor': classe_vencedor })
    partida += 1

# Mostra os resultados
relatorio_resultados()