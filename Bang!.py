from class_partita import Partita

partita = Partita
num = partita.verifica_num_giocatori()
partita.aggiungi_giocatori(num)
partita.assegna_ruoli(num)
partita.aggiungi_pf()
partita.inizia_partita()

