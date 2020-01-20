# test

Questo semplice progetto permette di verificare se una coppia (latitudine, longitudine) sia interna o meno al territorio calabrese.
Contenuto del progetto:

* test.py -----> file che gestisce la visualizzazione iniziale, crea il server (http://127.0.0.1:5000), analizza i dati in input forniti dal client e decide quale visualizzazione fornire nel browser. La visualizzazione nel browser dipende dal punto inserito: se interno all'area di riferimento verrà eseguito un file .html altrimenti un altro.

* indice.html -----> è il file che viene eseguito nel browser qualora il punto si trovi nel territorio calabrese. Il file è basato su Leaflet e Maptiler. In pratica si vedrà una mappa con setview iniziale sulla Calabria, la regione sarà delimitata da segmenti tratteggiati in rosso e vi sarà un marker indentificativo del punto inserito dal client. Nella console del browser vi sarà una stringa contenente il responso.

* indice1.html -----> è il file che viene eseguito nel browser qualora il punto non si trovi nel territorio calabrese. Il file è basato su Leaflet e Maptiler. Sostanzialmente è uguale al file descritto sopra, l'unica variante riguarda un messaggio di alert iniziale.
Si poteva evitare la duplicazione del file .html ma era giusto per far vedere che, potenzialmente, vi è la possibilità di eseguire diversi file .html a seconda delle condizioni.

Passi:

- Eseguire test.py inserendo latitudine e longitudine

- Aprire http://127.0.0.1:5000 nel browser

Qualora si volesse inserire un nuovo punto si deve arrestare il server e riavviare test.py, inserire le coordinate GPS, nonchè aggiornare il browser.


Ranges di riferimento:
- Latitudine [37.9, 40.15]
- Longitudine [15.62, 17.2]

Formato da utilizzare: xx.xxxxxx
