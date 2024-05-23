import requests
import json

endpoint = "https://dati.comune.milano.it/api/3/action/datastore_search?resource_id=1f2c6999-3532-4065-98fc-1fb6f722eaea&limit=5&q=title:jones"

def riceviFileJson(endpoint):
    risposta = requests.get(endpoint)

    if risposta.ok:
        datiJson = risposta.json()
        return datiJson
    else:
        print("Richiesta HTTP: ",risposta.status_code)
        raise Exception("Errore")

def stampaInformazioni():
    for r in record:
        if r["_id"] == int:
            print(json.dumps(r, indent=4))
            print("\t")



dati = riceviFileJson(endpoint)

campi = dati["result"]["fields"]
record = dati["result"]["records"]

print("\n\nI campi presenti nel file json sono: \n")
print(json.dumps(campi, indent= 4))

print("\n\n---------------INFORMAZIONI A PARTIRE DELL'ANNO 2014------------------ \n\n")
print("Prova\n\n")
stampaInformazioni()

