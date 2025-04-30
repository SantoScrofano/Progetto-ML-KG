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

Carico CSV da libreria Pandas. Uso df.info() per VISUALIZZARE la TIPOLOGIA dei VALORI DELLE COLONNE (float-boolean-iteger-str) & df.describe() la uso PER MEDIA E DEVIAZIONE STANDARD DI
OGNI COLONNA CON VALORI NUMERICI (PS: Ho separato il dataset tramite DF.iloc[:,[X]] (per colonne) IN 3 PARTI per visualizzare tutto e catturare gli screenshot.
              
LA MODA CON SCIPY.stats() DI COLONNE CON VALORI CATEGORIALI(testo): TRAMITE CODIFICA ONE HOT .get_dummies() vengono prodotte matricI con un numero di colonne pari al 
numero di categorie , quindi ricevo errore quando cerco la moda. Occorre rimuovere i valori nulli quando si decide di trasformare valori categoriali in 
numerici con .fillna(), ma fortunatamente questo dataset non ne ha. Unica soluzione rimane quindi quella dell'assegnare un valore numerico per ogni categoria tramite
dizionario di riferimento {a:1,b:2,...} con *funzione .map() e poi calcolare la MODA di ogni categoria delle colonne "SESSO", "LIVELLO ALLENAMENTO", "QUALITA' SONNO"
e tradotta nel commento col corrispettivo valore categoriale.
               
[Uso la funzione DF.columns.tolist() per visualizzare le intestazioni| NB: le intestazioni il cui titolo ha un accento vengono riportate con " , tutte le altre con ' .]
               
Analizzo infine con .corr() tra variabili e rappresentata con .heatmap() di Seaborn.
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




TRAIN/TEST
      Carico CSV e sostituisco variabili categoriche con numeriche. Imposto in X tutte le indipendenti tranne Surplus Calorico & Peso Finale e in Y l'ultima feautures 
      "VariazionePeso". Eseguo split train/test (75%/25%) da libreria SciKitLearn [visualizzare con grafico scatter sia Xtrain/Ytrain che Xtest/Ytest per assicurarci 
      che abbiano la stessa forma prima di procedere] e richiamo pure LinearRegression(). Creo la funzione e l'addestro .fit() con X e Y train , ottengo poi la 
      predizione di Y dando in pasto alla funzione .predict() i valori Xtest. Adesso non resta che confrontare Ypred con Ytest, così decido di vedere (per adesso solo
      graficamente) il rapporto che intercorre tra i 2 insiemi di valori con un grafico a punti .scatter() sovrapposto ad una retta diagonale creata con gli estremi di 
      Ypred e Ytest; quest'ultima rappresenta la massima corrispondenza tra i valori, cioè quando Ypred/Ytest=1. 



R2 + EQM SCALATI E NON -  

Con la trasformazione scalare delle variabili indipendenti si portano tutti i valori in un range compreso tra 0 e 1, così che i valori delle features
a confronto per i calcoli non siano troppo diversi tra loro . Quindi carico CSV , trasformo variabili categoriche in numeriche, split al 25% dei valori
di test da quelli di train e una volta ottenuta la funzione vado a predire i valori Y. Importo dalle metriche di SciKitLearn r2_score & mean_squared_error,
li calcolo e metto da parte i 2 risultati. Adesso richiamo sempre da SKLearn la funzione StandardScaler e scalo Xtrain & Xtest, il primo con scalare.fit_transform()
e il secondo con il comando scalare.transform(). Creo una nuova Regressione addestrando col valore Xtrain_scalare, poi allo stesso modo predico Y_scalare con .predict(Xtest_scalare). 
Ricalcolo r2 & EQM con il nuovo valore Ypred_scalare e Ytest ottenendo dei risulatati pressocchè simili a quelli non scalati poiché la scalarità è inutile con la regressione !!!





GRAFICI PIU' ELABORATI

 -piechart (torta) sesso partecipanti , ho prima usato la funzione DF.iloc[:,0].describe() per vedere la moda con relativa frequenza .
                      
- grafico dell'importanza delle features di XGBoost tramite chiamata della funzione da XGBoost, poi comando plot.iportance(modello , typo= gain)
  per crearla , infine rappresento con matplot. | NB non viene rappresentato il "Sesso" poiché ritenuto irrilevante sulle decisioni ad albero.
        

__________________________________________________________________________________________________________________________________________________________________________________________________________________


 CLUSTERING GERARCHICO CON K-MEANS - (APPR. NON SUPERVISIONATO) -                    
  
  Lo scopo sarà raggruppare i 100 individui in classi, a seconda il valore di aumento/perdita peso, trasformando un valore numerico in categoriale.
  Carico CSV e considero solo le due feautures "PesoIniziale" & "VariazionePeso" . Prima rappresento i punti con grafico a dispersione per vedere
 l'andamento dei valori. Importo Il metodo KMeans dalla libreria ScikitLearn e abbino tra loro i valori X e Y con la funzione .list(zip()) . Creo
  il campo inerzia e addestro la funzione KMeans con un ciclo for per un range di 5 valori ("penso" che siano questi il numero massimo di categorie
  visualizzando lo scatter iniziale). Richiamo la funzione inerzia con inertias.append(kmeans.inertia_) e la rappresento , trovando la parte di 
  grafico dove la curva inizia ad essere più lineare , il cosidetto "metodo a gomito", che indica il numero di cluster. Adattiamo dinuovo la 
  funzione kmeans , stavolta con il numero di cluster calcolato e rappresentiamo nuovamente un grafico a dispersione , impostando come 
  colorazione la sottofunzione kmeans.labels_ . I cluster ottenuti sono 4 , quindi potremmo raggruppareare i nostri individui in 4 gruppi ,
  considerando la variazione di peso dal valore di partenza, riassumento in termini più semplici i risultati raggiunti abbiamo individui con
  variazioni di peso : "esigue", "mediocri", "buone" e "strabilianti".

_________________________________________________________________________________________________________________________________________________________________________________________________________________

XGBOOST CON TUNING HYPERPARAMETRI, SALVATAGGIO CON PICKLE

Importo CSV con funzione Pandas, sostituisco variabili categoriche con numeriche e dopo aver assegnato le features a X e Y , divido con rapporto 75/25 i dati
di train e test con la funzione split da SciKitLearn. Importo la libreria XGBoost e imposto il mio modello con la funzione XGBRegressor(objective='reg:squared-
 error',n_estimators=50,learning_rate=0.1), dopo lo addestro con le variabili di training tramite comando .fit() . Predico i valori di Y con la funzione 
.predict(Xtest) e dopo li confronto con Ytest per calcolare r2 e l'errore quadratico medio , entrambe le funzioni importate da SciKitLearn. Per ottimizzare il
modello di regressione di XGBoost occorre trovare i giusti valori dei parametri che costituiscono il modello e per far ciò ci serviamo della funzione
GreadSearchCV di SciKitLearn. Creiamo un dizionario con il range di valori dei nostri parametri che vogliamo testare , sfortunatamente il mio pc non ha una 
grande potenza di calcolo e quindi per alleggerire la ricerca ho considerato solo alcuni parametri (n_estimators,max_depth,learning_rate) poiché nei tentativi
 con più combinazione di parametri Python crashava. Imposto la funzione griglia con il comando GridSearchCV(estimator=XGBOOST, parametri=dizionario, scoring=
 mse , cv=2, verbose=1, n_jobs=1) e dopo l'addestro con i valori di train usati prima. Con la funzione .best_params_ visualizzo i migliori valori dei parametri
 che ottimizzano la regressione e successivamente creo la funzione ottimizzata con il comando griglia.best_estimator_. Ottengo i nuovi valori di Y predetti 
dalla funzione ottimizzata e li riuso con Ytest per calcolare nuovamente le metriche di valutazione r2 e mse. Confrontando con i valori calcolati inizialmente
r2 è aumentato del 60%  e l'errore quadratico medio invece è stato dimezzato di 2,4 volte , segni evidenti che il tuning dei parametri effettuato sulla
funzione di regressione ha aumentato la potenza e l'attendibilità del modello. 

Il modello di regressione di XGBoost ottimizzato con i parametri è stato salvato tramite la libreria Pickle [with open("titolo file.pkl",wb) as f :
pickle.dump(nome funzione, f) ] . Chiudo e riapro Python , carico librerie numpy e pickle , scrivo una stringa col percorso del file .pkl salvato e 
carico il modello col comando [ with open (percorso file , "rb") as f : nome funzione = pickle.load(f) ] . Uso il comando modello.n_features_in_ per
visualizzare il numero di input richiesti dalla funzione appena caricata e creo un array Numpy con i 10 valori richiesti per testare il funzionamento
del modello caricato.

________________________________________________________________________________________________________________________________________________________________________________________________________________


CONCLUSIONI PER SCELTA MODELLO

Importo pandas , LinearRegression() di SciKitLearn e da Xgboost. Creo il modello di regressione multipla con SKL e ottengo le predizioni di Y
con i valori Xtest. Carico con Pickle la funzione di regressione XGB ottimizzata col tuning dei parametri, anche con questo modello
ottengo le previsioni di Y. Calcolo r2 e m_s_e di SKLearn con i valori YpredSKL/Ytest e YpredXGB/Ytest , stampo infine i risultati per trarre 
le conclusioni. Il valore R^2 del modello di SKL è negativo, quindi da risultati peggiori della semplice media aritmetica, inoltre l'
errore quadratico medio pari a 5,5819 è abbastanza elevato. Con il modello ottimizzato di XGBoost invece abbiamo
R^2= 0,9172 e msq= 0,4083 , mostrando chiaramente la superiorità e un adattamento maggiormente al nostro set di dati, predicendo
valori molto più precisi. Il programma si baserà quindi sul modello di XGBoost!!!

________________________________________________________________________________________________________________________________________________________________________________________________________________


PROGRAMMA I/O (3 FUNZIONI):

Ho cercato di riprodurre un sistema basilare, ma funzionante, senza curarmi di un aspetto con GUI curata, in grado di chiedere con una domanda specifica ogni
input necessario al funzionamento del modello di XGBoost da me creato. Il risultato di output è la variazione di peso calcolata dalla predizione del modello,
spiegata con una frase ad hoc nel caso si tratti di variazione positiva, negativa o impercettibile. Possiamo suddividere lo schema come un insieme di 
3 funzioni, prima però carico il modello creato con Pickle ed inserico frasi iniziali di benvenuto e saluti finali: 
                              
-RICHIESTA INPUT- ogni singola domanda vuole l'input che poi verrà indirizzato nell' array che daremo in pasto al modello.
-SPIEGA RISULTATO- condizione IF-ELIF-ELSE per spiegare all'utente l'output ottenuto. (uso valore assoluto per numero negativo, quando "si dimagrisce").
-MAIN- funzione principale che lega le antecedenti come estreme al modello XGB, gestendo l'intero flusso del programma. 
        Scrivo il comando [if name="main": main()] che permette l'utilizzo della funzione MAIN all'avvio del file.
 

ANDIAMO ONLINE...
 
Adesso siamo arrivati al momento della condivisione in rete del programma per renderlo fruibile a tutti. Il progetto iniziale prevedeva l'utilizzo di Flask per l'esecuzione online 
tramite API e il successivo deploy con Heroku. Il primo ostacolo affrontato per l'utilizzo di Flask, cioè la creazione della pagina in codice HTML (a me sconosciuto), mi ha fatto però
cambiare idea, così cercando delle alternative mi sono imbattuto nel servizio offerto dalla libreria Streamlit. Vorrei precisare che la scelta dell'utilizzo di Streamlit al posto della
combo Flask + Heroku è stata dettata principalmente dall'esigenza di accorciare i tempi di completamento del progetto e non per paura di apprendere nuovi linguaggi (HTML, CSS o JS).
Rimane comunque mio obbiettivo quello di dimostrare l'abilità nell'analisi dei dati con Python, tralasciando le nozioni da web-developer che occorrevano per utilizzare Flask.


STREAMLIT

dopo aver installato la libreria Streamlit con comando pip install da terminale, provo ad importarla sulla IDLE con il tipico comando import Steramlit as st.
Adesso non resta che modificare il programma locale creato in precedenza [Input/Output] e adattarlo all'uso su streamlit. Nella prima funzione, quella che si
occupa di ricevere gli input come risposta ad ogni corrispettiva domanda , modico la funzione print() con st.write() e i comandi per le features con 
st.number_input() . La 2° funzione che suddivide i risultati in tre categorie tramite if-elif-else rimane pressochè identica. La funzione MAIN con Streamlit
darà la possibilità di aggiungere un titolo alla pagina con st.title() e la creazione del pulsante che avvierà il modello per la previsione con st.button().
Il passo successivo doveva essere la visualizzazione dal browser in locale dopo aver avviato dal Prompt Windows il file appena creato , ma nonostante la procedura veniva
completata e riuscivo ad ottenere l'indirizzo con la porta utilizzata da Streamlit , una volta aperto da browser la pagina rimaneva bianca e svariati
tentativi. Sicuramente il pc obsoleto e il browser versione light non supportavano tali funzioni, così bypasso questa prova di collegamento locale e creo un account
GitHub ove caricare un file prova.py contenente un codice di richiamo Streamlit e la stampa di un titolo e un testo breve. Collego l'account GitHub a quello
Streamlit per avviare il file prova e stavolta tutto va a buon fine. Sostituisco il file prova con il programmino a 3 funzioni adattato per Streamlit , inserisco tutte le 
librerie utilizzate per questo progetto nel file Requirements.txt presente sulla repository di GitHub e infine avvio con successo da web il mio progetto 
funzionante! Tutte le piccole modifiche di codice per soli motivi estetici, successive al caricamento, verranno eseguite direttamente con la modifica codice da GitHub.


                          !!!  URL PROGETTO ML - DELTA KG :  https://progetto-ml-kg-uo9dcf2jbgnxmdqbmt8fba.streamlit.app/  !!!


Spero che il mio umile lavoro sia di vostro gradimento , attendo le vostre opinioni.

                                                                                                                                                                               
                                                                                                                                              SANTO SCROFANO.
                                                                                                                                                                                  
                                                                                                                                                                                  
                                                                                                                                                                                  
