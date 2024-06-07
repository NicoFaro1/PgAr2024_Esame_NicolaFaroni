from class_carta import Carta
from class_partita import Partita

class Mano:
    def __init__(self, numero: int, carta: Carta):
        self._numero = numero
        self._carta = carta
        self._carte = {}

    def aggiungi_carta(self, carta):
        self._carte[len(self._carte) + 1] = carta

    def mostra_mano(self):
        for numero, carta in self._carte.items():
            print(f"{numero}: {carta._nome}\n")

    def rimuovi_carta(self, numero: int, partita: Partita):
        carta_rimossa = self._carte.pop(numero)
        partita._lista_giocatori.append(carta_rimossa)
        