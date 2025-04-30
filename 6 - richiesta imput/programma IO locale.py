import numpy as np
import pickle
percorso = 'C:/Users/utente/Desktop/modello xgb ottimizzato.pkl'
with open (percorso, "rb") as f:
    modelloXGB= pickle.load(f)

def richiesta_input():
     print("_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_ì_^_^_^_^_^_^_^_^_^_^_^_^_")
     print(" Ciao , ti va di darmi delle info personali sul tuo stile di vita e così stimare la tua variazione di peso?  ")
     print("-------------------------------------------------------------------------------------------------------------------------")
     ETA = int(input(" INIZIAMO CON LA PRIMA DOMANDA: Quanti anni hai?  "))
     SESSO = int(input("SESSO BIOLOGICO: scrivi '0' se sei uomo OPPURE '1' se sei donna.  "))
     CALORIEASSUNTE = float(input("Quante calorie assumi in media ogni giorno?  "))
     CONSUMOCALORIE= float(input("Quante calorie bruci al giorno?  "))
     TEMPO = int(input("Quante settimane fa ti sei pesato l'ultima volta? "))
     ALLENAMENTO = float(input("Quanto ti alleni?  Scrivi '0.1' se non ti alleni mai/'0.3' se ti alleni poco/'0.6' se lo fai almeno 2 volte a settimana/'1' se pratichi sport agonistici  "))
     SONNO = float(input("Come dormi? Scrivi '0.25'(male) / '0.5'(meno di 7 ore) / '0.75'(8 ore) / '1' (sei un ghiro)  "))
     STRESS = int(input("STRESS: dove ti posizioni in una scala da 1 (relax) a 9 (sclero) per indicare il tuo livello?  "))
     PESO = float(input("Quanto pesavi l'ultima volta? (KG)  "))
     dati = np.array([[ETA,SESSO,CALORIEASSUNTE,CONSUMOCALORIE,TEMPO,ALLENAMENTO,SONNO,STRESS,PESO]])
     return dati

def spiega_risultato(predizione):
     print("Risultato:")
     if predizione > 0.1 :
         print(" Secondo il modello ingrasserai di",{predizione }, "KG! ")
     elif predizione < -0.1 :
         print(" Secondo il modello dimagrirai di",{abs(predizione)}, "KG! ")
     else:
         print("Avrai delle variazioni minime, pressocchè nulle. Sei costante nel tempo ! ")

def main():
     input = richiesta_input()
     predizione = modelloXGB.predict(input)[0]
     spiega_risultato(predizione)
     print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
     print("GRAZIE MILLE PER AVER")
     print("UTILIZZATO IL MIO PROGRAMMA")
     print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

if __name__ == "__main__":
     main()         
