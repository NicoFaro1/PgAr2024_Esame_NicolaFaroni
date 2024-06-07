from class_carta import Carta

class Arma (Carta):
    def __init__(self, nome: str, distanza: int, copie: list):
        self._nome = nome
        self._distanza = distanza
        self._copie = copie