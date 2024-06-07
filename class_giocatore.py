from class_carta import Carta
from class_mazzo import Mazzo
from class_arma import Arma
from class_mano import Mano

class Giocatore:
    def __init__(self, ruolo: str, sceriffo: bool, posizione: int, pf: int, id: int, equipaggiamento: list, abilità: str):
        self._ruolo = ruolo
        self._sceriffo = sceriffo
        self._posizione = posizione
        self._pf = pf
        self._id = id
        self._equipaggiamento = equipaggiamento
        self._abilità = abilità
        self._mano = Mano()

    def pesca_carte(self, mazzo: Mazzo) -> list:
        carta_pescata = mazzo.pesca_carte()
        if carta_pescata:
            self._mano.aggiungi_carta(carta_pescata)

    def gioca_carte(self, mazzo: Mazzo):
        bang_giocato = False
        print("Queste sono le carte che hai in mano: \n")
        Mano.mostra_mano()
        numero_carta = input("Seleziona la carta che vuoi giocare: \n")
        carta_giocata = Mano.rimuovi_carta(numero_carta)
        print(f"Hai giocato: {carta_giocata._nome}")  
        
    def scarta_carte(self, mazzo: Mazzo):
        while len(self._mano) > self._pf:
            print(f"{self._mano}\n")
            print(f"Devi scartare {len(self._mano)-self._pf}\n") 
            carta_da_scartare = input("Seleziona la carta che vuoi scartare: \n")
            if carta_da_scartare in self._mano:
                self._mano.remove(carta_da_scartare)
                mazzo._pila_scarti.append(carta_da_scartare)
            else:
                print("La carta selezionata non è nella tua mano, Riprova\n")

    def visualizza_pf(self):
        print(f"I tuoi PF attuali sono: {self._pf}")




    
        

        

        



