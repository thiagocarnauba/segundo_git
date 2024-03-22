
import random
from time import sleep
import os
from pathlib import Path
import json

class Piloto:
    def __init__(self, nome, pontos) -> None:
        self.nome = nome
        self.tempo = 0
        self.tempo_volta = 0
        self.pontos = pontos

    
    def realizar_volta(self, tempo_medio):
        self.tempo_volta = random.randint(tempo_medio - 5, tempo_medio) + (random.randint(1, 7) / 10)
        self.tempo += self.tempo_volta
        

def exibir_painel(pilotos: list) -> None:
    pilotos = sorted(pilotos, key=lambda piloto: piloto.tempo)

    for index, p in enumerate(pilotos):

        diferenca = pilotos[index].tempo - pilotos[index - 1].tempo
        p_formatado = p.nome.ljust(20, " ")
        if index:
            print(f'{index + 1}° {p_formatado}| Lap: {p.tempo_volta} | Diff: {diferenca: .3f}')
        else:
            print(f'{index + 1}° {p_formatado}| Lap: {p.tempo_volta} | Diff:  Líder')


def corrida(circuito: dict, voltas: int, pilotos: list) -> None:
    for volta in range(1, voltas + 1):
        os.system('cls')
        nome_gp = circuito['circuito']
        print(f'\n-------- VOLTA {volta}/{voltas} | GP {nome_gp} -----------\n')
        for piloto in pilotos:
            piloto.realizar_volta(circuito['tempo_medio'])
            
        
        exibir_painel(pilotos)
        sleep(2)

    #zerar tempo dos pilotos
    for index, p in enumerate(pilotos):
        p.tempo = 0

        if index == 0:
            p.pontos += 25
        elif index == 1:
            p.pontos += 18
        elif index == 2:
            p.pontos += 15    
        elif index == 3:
            p.pontos += 12
        elif index == 4:
            p.pontos += 10 
        elif index == 5:
            p.pontos += 8  
        elif index == 6:
            p.pontos += 6 
        elif index == 7:
            p.pontos += 4
        elif index == 8:
            p.pontos += 2
        

    return


def salvar(pilotos):
    with open('pilotos.json', 'w') as file:
        json.dump(pilotos, file)

#Inicio do código 
CAMINHO_PILOTO = Path(__file__).parent
CAMINHO_PILOTO = CAMINHO_PILOTO / 'pilotos.json'

CAMINHO_CIRCUITO = Path(__file__).parent
CAMINHO_CIRCUITO = CAMINHO_CIRCUITO / 'grandpix.json'

CAMINHO_SAVE = Path(__file__).parent
CAMINHO_SAVE = CAMINHO_SAVE / 'save.json'

with open(CAMINHO_SAVE, 'r') as file:
    circuito_atual = json.load(file)
    circuito_atual = circuito_atual['corrida_atual']

with open(CAMINHO_CIRCUITO, 'r', encoding='utf-8') as file:
    circuitos = json.load(file)

pilotos = []

with open(CAMINHO_PILOTO, 'r') as file:
    nomes = json.load(file)
    for p in nomes:
        piloto = Piloto(p['nome'], p['pontos'])
        pilotos.append(piloto)


for gp in range(circuito_atual, len(circuitos)):

    circuito = circuitos[gp]['circuito']
    voltas = circuitos[gp]['voltas']
    tempo_medio = circuitos[gp]['tempo_medio']

    print(circuitos[gp])
    corrida(circuitos[gp], voltas, pilotos)








