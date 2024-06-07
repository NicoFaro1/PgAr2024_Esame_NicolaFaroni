from class_partita import Partita

partita = Partita
num_giocatori = 0
num_giocatori = input("Inserisci il numero di giocatori: ")
while num_giocatori < 4 or num_giocatori > 7:
    num_giocatori = int(input("Hai sbagliato ad inserire il numero di giocatori, riprova (4-7)"))

partita.aggiungi_giocatori(num_giocatori)
partita.assegna_ruoli(num_giocatori)
partita.aggiungi_pf()
partita.inizia_partita()

