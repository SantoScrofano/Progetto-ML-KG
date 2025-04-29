import streamlit as st
import numpy as np
import pickle

percorso = 'modello xgb ottimizzato.pkl'
with open (percorso, "rb") as f:
    modelloXGB= pickle.load(f)

def richiesta_input():
     st.write("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
     st.write(" Ciao , ti va di darmi delle info personali sul tuo stile di vita e così stimare la tua variazione di peso?  ")
     st.write("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-")
     ETA = st.number_input(" INIZIAMO CON LA PRIMA DOMANDA: Quanti anni hai?  ")
     SESSO = st.number_input("SESSO BIOLOGICO: scrivi '0' se sei uomo OPPURE '1' se sei donna.  ")
     CALORIEASSUNTE = st.number_input("Quante calorie assumi in media ogni giorno?  ")
     CONSUMOCALORIE= st.number_input("Quante calorie bruci al giorno?  ")
     TEMPO = st.number_input("Quante settimane fa ti sei pesato l'ultima volta? ")
     ALLENAMENTO = st.number_input("Quanto ti alleni?  Scrivi '0.1' se non ti alleni mai/'0.3' se ti alleni poco/'0.6' se lo fai almeno 2 volte a settimana/'1' se pratichi sport agonistici  ")
     SONNO = st.number_input("Come dormi? Scrivi '0.25'(male) / '0.5'(meno di 7 ore) / '0.75'(8 ore) / '1' (sei un ghiro)  ")
     STRESS = st.number_input("STRESS: dove ti posizioni in una scala da 1 (relax) a 9 (sclero) per indicare il tuo livello?  ")
     PESO = st.number_input("Quanto pesavi l'ultima volta? (KG)  ")
     
     dati = np.array([ETA,SESSO,CALORIEASSUNTE,CONSUMOCALORIE,TEMPO,ALLENAMENTO,SONNO,STRESS,PESO])
     return dati

def spiega_risultato(predizione):
     st.write("Risultato:")
     if predizione > 0.1 :
         st.write(" Secondo il modello ingrasserai di (predizione) KG! ")
     elif predizione < -0.1 :
         st.write(" Secondo il modello dimagrirai di (predizione) KG! ")
     else:
         st.write("Avrai delle variazioni minime, pressocchè nulle. Sei costante nel tempo ! ")

def main():
     st.title(" :) PREVEDO LA TUA VARIAZIONE DI MASSA CORPOREA :) ")
     input = richiesta_input()

     if st.button('CALCOLO.....'): 
         predizione = modelloXGB.predict([input])[0]  
         spiega_risultato(predizione)
         
st.write(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
st.write("GRAZIE MILLE IN ANTICIPO PER AVER")
st.write("UTILIZZATO IL MIO PROGRAMMA")
st.write(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

if __name__ == "__main__":
     main()         
