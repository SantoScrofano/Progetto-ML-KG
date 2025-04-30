# Progetto MachineLearning - deltaKG 

URL DOWNLOAD DATASET (KAGGLE) --->  https://www.kaggle.com/datasets/abdullah0a/comprehensive-weight-change-prediction/data

Lo scopo di questo progetto sarà quello di presentare la variazione (aumento/perdita) di peso ideale che l'utente avrebbe dovuto conseguire in un lasso di tempo da lui indicato e 
prendendo come base i parametri sul suo stile di vita. Confrontare poi il risultato ottenuto con la variazione di peso realizzata e riuscendo così a capire se è andato oltre o meno le aspettative, adottando comportamenti errati o in linea con le previsioni. Quando lo scostamento (reale) dal risultato calcolato sarà considerevole, questo programmino potrà essere un 
primo segnale di allert per il nostro stato generale di salute, considerandolo a tutti gli effetti un feedback in campo health. L'algoritmo sarà addestrato partendo dai 100 campioni(righe) presenti nel dataset scaricato dal sito Kaggle. Il nesso tra i risultati previsti e la realtà sarà inverosimile poichè sarebbe impossibile considerare solo i fattori registrati nelle 
colonne(feautures), in quanto nella vita di tutti i giorni coesistono moltissime altre variabili che potrebbero influenzare il risultato finale. Detto ciò, la creazione di tal 
progetto non vuole sostituirsi al lavoro di nessun medico / nutrizionista / personal trainer, ma servirà solamente a testare le mie abilità di elaborazione e rappresentazione dati con 
Python. Il sottoscritto si declina  da ogni responsabilità per eventuali danni causati da un utilizzo improprio e/o scorretto di questo programma da me creato.

DATA CLEANING & FEAUTURE ENGINEERING : la colonna originale VariazionePeso presentava valori negativi anomali (controlla tu stesso scaricando l'originale dal 
link sopra), pertanto è stata sostituita con una nuova ottenuta dalla formula di sottrazione: PesoFinale - PesoIniziale; per far ciò su excel ho
trasformato il formato dati della colonna in numero e sostituito da tutti i numeri decimali il punto con la virgola (altrimenti non potevo eseguire la funzione di sottrazione). 
L'operazione inversa , cioè rimettere i punti al posto delle virgole, è stata eseguita sul file CSV tramite la funzione sostituisci di Blocconote per far in modo
che la libreria Pandas leggesse e visualizzasse in modo chiaro il CSV in dataframe, poichè inizialmente la visualizzazione appariva distorta a causa del separatore di valori ";".
I numeri decimali del nuovo CSV non verranno considerati tali nemmeno su PowerBI poiché, così come Excel, considera solo la virgola come separatore di numeri decimali.
Per adattare meglio i valori alla mia comprensione durante il lavoro di pulizia dei dati, ho preferito tradurre le intestazioni del dataset dall'inglese all'
italiano con la funzione sostituisci di Excel e convertire le libbre in kilogrammi creando 3 nuove colonne con una semplice formula di conversione (kg = libbra/2,20462), 
poi arrotondata a 2 cifre decimali. Infine è stata effettuata la rimozione della colonna "ID Partecipante" perché superflua visto che preferisco navigare sul dataframe dai valori 
degli indici (0-99) e ho ordinato le restanti colonne a mio piacimento e senso logico. Ho tradotto in italiano, con la funzione "sostituisci valori", pure i dati categoriali delle 
colonne: "Livello attività fisica" & "Qualità sonno", successivamente sono stati pure trasformati in dati numerici con *2 diverse funzioni. Ordinando in senso crescente la colonna 
"Daily caloric surplus/deficit", data dalla differenza tra calorie assunte e calorie consumate , si può notare che non esistono valori negativi e quindi nessuno dei 100 partecipanti
versa in una condizione di deficit calorico, pertanto l'intestazione verrà rinomata solo come "Surplus calorico". La colonna "SURPLUS CALORICO" non verrà considerata nella regressione poiché i suoi dati rappresentano la differenza tra i rispettivi valori, finali e iniziali. La feature "PESO FINALE" potrebbe invece addestrare il modello in funzione della sottrazione da
essa dal peso inziale, ma poiché il nostro output prevede di calcolare la variazione in funzione del comportamento dell'individuo è opportuno lasciare solo la variabile nota "Peso iniziale" ed evitare situazioni di data leakage (dati superflui che possono confondere il modello) non considerando il "Peso Finale" . 


___________________________________________________________________________________________________________________________________________________________________________________________



