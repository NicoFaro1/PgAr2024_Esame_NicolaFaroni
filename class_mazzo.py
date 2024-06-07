import random
import funzioni_gioco as fg
from class_arma import Arma
from class_carta import Carta

class Mazzo:
    def __init__(self, num_carte: int, pila_scarti: list):
        self._num_carte = num_carte
        self._pila_scarti = pila_scarti
        self._carte = []

    def crea_mazzo(self):
        for i in range(50):
            for carta_info in fg.leggi_json(r'listaCarte.json')["carte"]:
                if carta_info["nome"] == "BANG!":
                    carta = Carta(False, carta_info["nome"], carta_info["descrizione"])
                self._carte.append(carta)
        for i in range(24):
            for carta_info in fg.leggi_json(r'listaCarte.json')["carte"]:
                if carta_info["nome"] == "Mancato!":
                    carta = Carta(False, carta_info["nome"], carta_info["descrizione"])
                self._carte.append(carta)
        for i in range(3):
            for carta_info in fg.leggi_json(r'listaCarte.json')["armi"]:
                if carta_info["nome"] == "Schofield":
                    carta = Arma(carta_info["nome"], carta_info["distanza"])
                self._carte.append(carta)
            for carta_info in fg.leggi_json(r'listaCarte.json')["armi"]:
                if carta_info["nome"] == "Remington":
                    carta = Arma(carta_info["nome"], carta_info["distanza"])
                self._carte.append(carta)
            for carta_info in fg.leggi_json(r'listaCarte.json')["armi"]:
                if carta_info["nome"] == "Rev.Carabine":
                    carta = Arma(carta_info["nome"], carta_info["distanza"])
                self._carte.append(carta)
            for carta_info in fg.leggi_json(r'listaCarte.json')["armi"]:
                if carta_info["nome"] == "Whinchester":
                    carta = Arma(carta_info["nome"], carta_info["distanza"])
                self._carte.append(carta)
        return self._carte

    def mescola(self):
        self._carte.extend(self._pila_scarti)
        random.shuffle(self._carte)
        self._pila_scarti.clear()

    def pesca_carte(self) -> Carta:
        if self._carte:
            return self._carte.pop(0)

    
