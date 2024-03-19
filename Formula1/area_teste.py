
from pathlib import Path
import json

CAMINHO_SAVE = Path(__file__).parent
CAMINHO_SAVE = CAMINHO_SAVE / 'save.json'

with open(CAMINHO_SAVE, 'r') as file:
    circuito_atual = json.load(file)
    print(circuito_atual)