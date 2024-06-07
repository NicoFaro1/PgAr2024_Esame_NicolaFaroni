from class_mazzo import Mazzo
from class_mano import Mano
from class_carta import Carta
from class_arma import Arma

class Giocatore:
    def __init__(self, ruolo: str, sceriffo: bool, posizione: int, pf: int, id: int, equipaggiamento: Arma, abilità: str, sbleuri: int):
        self._ruolo = ruolo
        self._sceriffo = sceriffo
        self._posizione = posizione
        self._pf = pf
        self._id = id
        self._equipaggiamento = equipaggiamento
        self._abilità = abilità
        self._mano = Mano()
        self._sbleuri = sbleuri

    def pesca_carte(self, mazzo: Mazzo) -> list:
        carta_pescata = mazzo.pesca_carte()
        if carta_pescata:
            self._mano.aggiungi_carta(carta_pescata)

    def gioca_carte(self) -> Carta:
        print("Queste sono le carte che hai in mano: \n")
        Mano.mostra_mano()
        numero_carta = input("Seleziona la carta che vuoi giocare: \n")
        carta_giocata = Mano.rimuovi_carta(numero_carta)
        print(f"Hai giocato: {carta_giocata._nome}")
        return carta_giocata  

    def visualizza_pf(self):
        print(f"I tuoi PF attuali sono: {self._pf}")
        



    
        

        

        



