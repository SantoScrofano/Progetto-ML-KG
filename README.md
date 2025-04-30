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

FUNZIONI BASE    

               Carico CSV da Pandas. Uso df.info() per VISUALIZZARE la TIPOLOGIA dei VALORI DELLE COLONNE (float-boolean-iteger-str) df.describe() la uso PER MEDIA E DEVIAZIONE STANDARD DI
               OGNI COLONNA CON VALORI NUMERICI (PS: Ho separato il dataset tramite DF.iloc[:,[X]] (per colonne) IN 3 PARTI per visualizzare tutto e catturare gli screenshot.
              
               MODA CON SCIPY.stats() DI COLONNE CON VALORI CATEGORIALI(testo): TRAMITE CODIFICA ONE HOT .get_dummies() vengono prodotte matricI con un numero di colonne pari al 
               numero di categorie , quindi ricevo errore quando cerco la moda. Occorre rimuovere i valori nulli quando si decide di trasformare valori categoriali in 
               numerici con .fillna(), ma fortunatamente questo dataset non ne ha. Unica soluzione rimane quindi quella dell'assegnare un valore numerico per ogni categoria tramite
               dizionario di riferimento {a:1,b:2,...} con *funzione .map() e poi calcolare la MODA di ogni categoria delle colonne "SESSO", "LIVELLO ALLENAMENTO", "QUALITA' SONNO"
               e tradotta nel commento col corrispettivo valore categoriale.
               
               [Uso la funzione DF.columns.tolist() per visualizzare le intestazioni| NB: le intestazioni il cui titolo ha un accento vengono riportate con " , tutte le altre con ' .]
               
               .corr() tra variabili e rappresentata con .heatmap() di Seaborn.
_____________________________________________________________________________________________________________________________________________________________________________________________________

              
REGRESSIONE MULTIPLA -       
                         Ho sostituito le variabili categoriali in variabili numeriche tramite il *comando DF.replace([categoria1,categoria2,...],[sostitutonum1,sostitutonum2,...],
                         inplace=True); se omettevo il comando inplace dovevo assegnare un nuovo nome al dataframe creato, così invece ho modificato l'originale . 
                         Ho assegnato a X tutte le variabili indipendenti tranne "SurplusCalorico" e "Peso finale", ad Y la variabile dipendente "VariazionePeso". La regressione è                 
                         stata richiamata alla libreria SciKitLearn e l'ho addestrata con X e Y tramite comando .fit(X,y) , dopo ho calcolato il coefficiente di regressione di ogni variabile
                         indipendente per vedere quanto incide ognuna sul risultato Y . Infine ho predetto un valore Y inserendo i miei 9 ipotetici valori vitali e nonostante il 
                         messaggio d'errore ad ogni tentativo ho ottenuto un valore Ypred. Infine ho pure provato altre combinazioni di input modificando quelli che avevano un 
                         coefficiente più grande per constatare la maggiore variazione di Y.


* entrambe i comandi sono stati usati per sostituire i valori categoriali in numerici, cambia solo il campo di applicazione: la funzione .map() può cambiare i valori solo ad una colonna per volta con l'ausilio di un dizionario, mentre la funzione .replace() riesce a sostituire con un unico comando tutti i valori del dataset che voglio.




         TRAIN/TEST  -  Carico CSV e sostituisco variabili categoriche con numeriche. Imposto in X tutte le indipendenti tranne Surplus Calorico & Peso Finale e in Y l'ultima feautures 
                        "VariazionePeso". Eseguo split train/test (75%/25%) da libreria SciKitLearn [visualizzare con grafico scatter sia Xtrain/Ytrain che Xtest/Ytest per assicurarci 
                        che abbiano la stessa forma prima di procedere] e richiamo pure LinearRegression(). Creo la funzione e l'addestro .fit() con X e Y train , ottengo poi la 
                        predizione di Y dando in pasto alla funzione .predict() i valori Xtest. Adesso non resta che confrontare Ypred con Ytest, così decido di vedere (per adesso solo
                        graficamente) il rapporto che intercorre tra i 2 insiemi di valori con un grafico a punti .scatter() sovrapposto ad una retta diagonale creata con gli estremi di
                        Ypred e Ytest; quest'ultima rappresenta la massima corrispondenza tra i valori, cioè quando Ypred/Ytest=1. 



R2 + EQM SCALATI E NON -  Con la trasformazione scalare delle variabili indipendenti si portano tutti i valori in un range compreso tra 0 e 1, così che i valori delle features
                          a confronto per i calcoli non siano troppo diversi tra loro . Quindi carico CSV , trasformo variabili categoriche in numeriche, split al 25% dei valori
                          di test da quelli di train e una volta ottenuta la funzione vado a predire i valori Y. Importo dalle metriche di SciKitLearn r2_score & mean_squared_error,
                          li calcolo e metto da parte i 2 risultati. Adesso richiamo sempre da SKLearn la funzione StandardScaler e scalo Xtrain & Xtest, il primo con scalare.fit_transform()
                          e il secondo con il comando scalare.transform(). Creo una nuova Regressione addestrando col valore Xtrain_scalare, poi allo stesso modo predico Y_scalare con .predict(Xtest_scalare). 
                          Ricalcolo r2 & EQM con il nuovo valore Ypred_scalare e Ytest ottenendo dei risulatati pressocchè simili a quelli non scalati poiché la scalarità è inutile con la regressione !!!





GRAFICI PIU' ELABORATI:   
                       -piechart (torta) sesso partecipanti , ho prima usato la funzione DF.iloc[:,0].describe() per vedere la moda con relativa frequenza .
                      
                       - grafico dell'importanza delle features di XGBoost tramite chiamata della funzione da XGBoost, poi comando plot.iportance(modello , typo= gain) per crearla , infine
                         rappresento con matplot. | NB non viene rappresentato il "Sesso" poiché ritenuto irrilevante sulle decisioni ad albero.
        

__________________________________________________________________________________________________________________________________________________________________________________________________________________


         CLUSTERING GERARCHICO  -  Lo scopo sarà raggruppare i 100 individui in classi, a seconda il valore di aumento/perdita peso, trasformando un valore numerico in categoriale.
          CON K.MEAN - (APPR.      Carico CSV e considero solo le due feautures "PesoIniziale" & "VariazionePeso" . Prima rappresento i punti con grafico a dispersione per vedere
          NON SUPERVISIONATO)      l'andamento dei valori. Importo Il metodo KMeans dalla libreria ScikitLearn e abbino tra loro i valori X e Y con la funzione .list(zip()) . Creo
                                   il campo inerzia e addestro la funzione KMeans con un ciclo for per un range di 5 valori ("penso" che siano questi il numero massimo di categorie
                                   visualizzando lo scatter iniziale). Richiamo la funzione inerzia con inertias.append(kmeans.inertia_) e la rappresento , trovando la parte di 
                                   grafico dove la curva inizia ad essere più lineare , il cosidetto "metodo a gomito", che indica il numero di cluster. Adattiamo dinuovo la 
                                   funzione kmeans , stavolta con il numero di cluster calcolato e rappresentiamo nuovamente un grafico a dispersione , impostando come 
                                   colorazione la sottofunzione kmeans.labels_ . I cluster ottenuti sono 4 , quindi potremmo raggruppareare i nostri individui in 4 gruppi ,
                                   considerando la variazione di peso dal valore di partenza, riassumento in termini più semplici i risultati raggiunti abbiamo individui con
                                   variazioni di peso : "esigue", "mediocri", "buone" e "strabilianti".

_________________________________________________________________________________________________________________________________________________________________________________________________________________
