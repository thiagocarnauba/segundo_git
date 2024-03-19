from time import sleep
import random
from threading import Thread


def corrida(piloto):
    tempo_total = 0

    for volta in range(1, 3):
        tempo_volta = random.randint(4, 8) 
        tempo_total += tempo_volta
        sleep(tempo_volta)
        print(f'{piloto}, volta {volta}: {tempo_volta}\n')
    
    print(f'{piloto}: Tempo:{tempo_total}')


t1 = Thread(target=corrida, args=('Max',))
t2 = Thread(target=corrida, args=('Hamilton',))

t1.start()
t2.start()

while t1.is_alive() or t2.is_alive():
    ...


if t1.is_alive:
    print(t1.__dict__)
else:
    print(t2.__dict__)

print('Teste de GIT')


