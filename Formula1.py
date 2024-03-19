
import random
from time import sleep
import os

class Piloto:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.tempo = 0
        self.tempo_volta = 0
    
    def __repr__(self) -> str:
        return f'{self.nome}'
    
    def realizar_volta(self):
        self.tempo_volta = random.randint(110, 115) + (random.randint(1, 7) / 10)
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



nomes = [
    "Max Verstappen",
    "Sergio Pérez",
    "Charles Leclerc",
    "George Russell",
    "Carlos Sainz",
    "Fernando Alonso",
    "Lando Norris",
    "Lewis Hamilton",
    "Daniel Ricciardo"
]
pilotos = []

for nome in nomes:
    piloto = Piloto(nome)
    pilotos.append(piloto)

for volta in range(1, 11):
    os.system('cls')
    print(f'\n--------- VOLTA {volta} ---------\n')
    for piloto in pilotos:
        piloto.realizar_volta()
        
    
    exibir_painel(pilotos)
    sleep(10)



#for p in pilotos:
#   p_formatado = p.nome.ljust(10, " ")
#   print(f'{p_formatado}| Tempo Volta: 1.208 | Volta:10')

