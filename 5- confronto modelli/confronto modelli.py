Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
from sklearn.linear_model import LinearRegression
import xgboost as xgb
DF= pd.read_csv(r'C:\Users\utente\Desktop\variazione_peso.csv', encoding='ISO-8859-1')
DF.replace(["M", "F","Sedentario","Basso","Medio","Alto","Sufficiente","Bassa","Buona","Ottima"],[0,1,0.1,0.3,0.6,1,0.25,0.5,0.75,1],inplace=True)

Warning (from warnings module):
  File "<pyshell#4>", line 1
FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
DF.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 12 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   ETA'                      100 non-null    int64  
 1   SESSO                     100 non-null    int64  
 2   CALORIE ASSUNTE           100 non-null    float64
 3   CALORIE BRUCIATE(RIPOSO)  100 non-null    float64
 4   SURPLUS CALORICO          100 non-null    float64
 5   SETTIMANE VARIAZIONE      100 non-null    int64  
 6   LIVELLO ALLENAMENTO       100 non-null    float64
 7   QUALITA' SONNO            100 non-null    float64
 8   LIVELLO STRESS            100 non-null    int64  
 9   PESO INIZIALE             100 non-null    float64
 10  PESO FINALE               100 non-null    float64
 11  VARIAZIONE PESO           100 non-null    float64
dtypes: float64(8), int64(4)
memory usage: 9.5 KB
>>> X=DF.iloc[:,[0,1,2,3,5,6,7,8,9]]
>>> y= DF.iloc[:,11]
>>> from sklearn.model_selection import train_test_split
>>> Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,test_size=0.25)
>>> modelloSKL = LinearRegression()
>>> modelloSKL.fit(Xtrain,Ytrain)
LinearRegression()
>>> YpredSKL = modelloSKL.predict(Xtest)
>>> #CARICO MODELLO XGBOOST OTTIMIZZATO
>>> import pickle
>>> percorso= 'C:/Users/utente/Desktop/modello xgb ottimizzato.pkl'
>>> with open (percorso, "rb") as f:
...     modelloXGB= pickle.load(f)
... 
...     
>>> YpredXGB = modelloXGB.predict(Xtest)
>>> from sklearn.metrics import r2_score, mean_squared_error
>>> r2SKL= r2_score(Ytest,YpredSKL)
>>> mseSKL = mean_squared_error (Ytest,YpredSKL)
>>> r2XGB= r2_score(Ytest,YpredXGB)
>>> mseXGB = mean_squared_error (Ytest,YpredXGB)
>>> print (" Il valore R^2 del modello di regressione di SciKitLearn è pari a: " , r2SKL , " , del modello di XGBoost è invece pari a: " , r2XGB, " \n L'errore quadratico medio su SciKitLearn è uguale a: " , mseSKL , " , mentre su XGBoost è: " , mseXGB)
 Il valore R^2 del modello di regressione di SciKitL è pari a:  -0.1317606878194051  , del modello di XGBoost è invece pari a:  0.9172117443836536  
 L'errore quadratico medio su SciKitLearn è uguale a:  5.581699933447526  , mentre su XGBoost è:  0.40830115927982696
