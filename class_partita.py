from class_mazzo import Mazzo
from class_giocatore import Giocatore
import random

class Partita:
    def __init__(self, num_giocatori: int, lista_giocatori: list, turno: int, pila_scarti: list, fine_partita: bool):
        self._num_giocatori = num_giocatori
        self._lista_giocatori = lista_giocatori
        self._turno = turno
        self._mazzo = Mazzo.crea_mazzo()
        self._pila_scarti = pila_scarti
        self._fine_partita = fine_partita

    def aggiungi_giocatori(self):
        num_giocatori = 0
        print("Inserisci il numero di giocatori: ")
        while num_giocatori < 4 or num_giocatori > 7:
            num_giocatori = int(input("Hai sbagliato ad inserire il numero di giocatori, riprova (4-7)"))
        ruoli = self.assegna_ruoli(num_giocatori)
        self._lista_giocatori = [Giocatore(ruoli[i], ruoli[i] == 'Sceriffo', i) for i in range(num_giocatori)]
        random.shuffle(self._lista_giocatori[1:])

    def assegna_ruoli(self, num_giocatori: int):
        ruoli = ["Sceriffo", "Rinnegato"] + ["Fuorilegge"]*2
        if num_giocatori == 5:
            ruoli.append("Vice")
        if num_giocatori == 6:
            ruoli.append("Fuorilegge")
        if num_giocatori == 5:
            ruoli.append("Vice")
        random.shuffle(ruoli[1:])
        return ruoli

    def prendi_posizioni_giocatori(self):
        posizioni = []
        for giocatore in self._lista_giocatori:
            posizioni.append(giocatore._posizione)
        return posizioni
    
    def calcola_distanza(self, giocatore1: Giocatore, giocatore2: Giocatore):
        num_giocatori = len(self._lista_giocatori)
        distanza_orario = (giocatore1._posizione - giocatore2._posizione) % num_giocatori   # Questo garantisce che venga ritornato un valore positivo
        distanza_antiorario = num_giocatori - distanza_orario
        return min(distanza_orario, distanza_antiorario)
    
    def visualizza_distanza(self, giocatore1: Giocatore, giocatore2: Giocatore):
        if giocatore1._posizione == giocatore2._posizione:
            print(f"Il giocatore {giocatore1._id} è a distanza 0 da {giocatore2._id}")
        else:
            # Calcola la distanza utilizzando una funzione della classe Partita
            distanza = self.calcola_distanza(giocatore1, giocatore2)
            print(f"Il giocatore {giocatore1._id} è a distanza {distanza} da {giocatore2._id}")

    def verifica_condizioni_fine_partita(self, giocatore_eliminato: Giocatore):
        if giocatore_eliminato._ruolo == "Sceriffo":
            rinnegato_in_gioco = False
            altri_giocatori_vivi = False
            for giocatori in self._lista_giocatori:
                if giocatori._ruolo == "Rinnegato" and giocatori._pf > 0:
                    rinnegato_in_gioco = True
                elif giocatori._pf > 0:
                    altri_giocatori_vivi = True
            if altri_giocatori_vivi and not rinnegato_in_gioco:
                print("I fuorilegge hanno vinto!")
            if not altri_giocatori_vivi and rinnegato_in_gioco:
                print("Il rinnegato ha vinto!")
        if giocatore_eliminato._ruolo == "Fuorilegge" or giocatore_eliminato._ruolo == "Rinnegato":
            rinnegato_vivo = False
            fuorilegge_vivi = False
            for giocatori in self._lista_giocatori:
                if giocatori._ruolo == "Rinnegato" and giocatori._pf > 0:
                    rinnegato_vivo = True
                if giocatori._ruolo == "Fuorilegge" and giocatori._pf > 0:
                    fuorilegge_vivi = True
            if not fuorilegge_vivi and not rinnegato_vivo:
                for giocatori in self._lista_giocatori:
                    if giocatori._ruolo == "Sceriffo" or giocatori._ruolo == "Vice":
                        print("Lo sceriffo e i suoi Vice hanno vinto!")

    def elimina_giocatore(self, giocatore: Giocatore):
        if giocatore._pf <= 0:
            print(f"Il giocatore eliminato aveva il ruolo di {giocatore._ruolo}")
            for carta in len(giocatore._mano):
                giocatore._mano.remove(carta)
                self._pila_scarti.append(carta)
            self.verifica_condizioni_fine_partita(giocatore)

