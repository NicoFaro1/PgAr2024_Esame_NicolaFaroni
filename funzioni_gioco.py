import json

def leggi_json(filepath: str):
    with open(filepath, "r") as file:
        dati_carte = json.load(file)
    return dati_carte