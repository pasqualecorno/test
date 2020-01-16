from flask import Flask, render_template
import os

prova=Flask("__name__")

clear = lambda: os.system('cls') # Pulisco prompt dei comandi in Windows
clear()                          #

# Inserisci da input i valori di latitudine e longitudine
lat=input("\n\nCiao, questo programma verifica che una coppia Latitudine-Longitudine sia interna al territorio calabrese o meno. \n!!! N.B. !!! Non sono ammessi caratteri.\n \n Inserisci la Latitudine \n >. Lat: ")
lng=input("\nBene, ora inserisci la Longitudine. \n >. Lng: ")
print("\n\n\nPer avere una visualizzazione della mappa vai su http://127.0.0.1:5000/ \n\n\n")


@prova.route("/")

def funzione():        
    Lat=float(lat)  # Converto i dati da input (stringhe) in float
    Lng=float(lng)  #

    # Controllo grossolano sui dati GPS inseriti (Verifico che in punto si trovi o meno in un rettangolo che racchiude la Calabria)
    if Lat>37.9 and Lat<40.15:
        if Lng>15.62 and Lng<17.22:
            #print("ok")
            
            # Inizializzo una mappa (indice.html) e gli passo delle variabili. Il file .html si occuperà della visualizzazione di un marker nella posizione indicata dal client
            return render_template("indice.html", coord1=Lat, coord2=Lng, messaggio="Il punto "+ "(" +lat +", "+ lng +")" + " è in Calabria o in acque calabresi!")
            
    else:
        # Inizializzo una mappa (indice1.html) che fa la stessa cosa. Inoltre mostra un Alert al client
        return render_template("indice1.html", coord1=Lat, coord2=Lng, messaggio="Il punto "+ "(" +lat +", "+ lng +")" + " non è in Calabria o in acque calabresi!")
        
if __name__ == "__main__":
    
    #prova.run(debug=True)      // Qualora si richiedesse di non dover riavviare manualmente il server ad ogni cambiamento del file test.py
    prova.run()
