Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
DF= pd.read_csv(r'C:\Users\utente\Desktop\variazione_peso.csv', encoding='ISO-8859-1')
DF.replace(["M", "F","Sedentario","Basso","Medio","Alto","Sufficiente","Bassa","Buona","Ottima"],[0,1,0.1,0.3,0.6,1,0.25,0.5,0.75,1],inplace=True)

Warning (from warnings module):
  File "<pyshell#5>", line 1
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
X=DF.iloc[:,[0,1,2,3,5,6,7,8,9]]
y= DF.iloc[:,11]
# SPLIT DATI PER REGRESSIONE
from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,test_size=0.25)
modello= LinearRegression()
modello.fit(Xtrain,Ytrain)
LinearRegression()
print(modello.coef_)
[-8.00827744e+00 -3.95484613e+02  2.58529310e-03 -1.60854881e+00
 -7.38328878e-02 -9.27615166e-01  1.49808938e+00 -8.98247797e-01
  3.53877339e+01]
Ypred = modello.predict(Xtest)
Ytest.describe()
count    25.000000
mean     -1.407200
std       2.223598
min      -5.670000
25%      -2.990000
50%      -1.090000
75%       0.540000
max       1.630000
Name: VARIAZIONE PESO , dtype: float64
A= np.array([-6,2])
B= np.array([-6,2])
plt.scatter(Ypred,Ytest)
<matplotlib.collections.PathCollection object at 0x000002E31AF51DC0>
plt.plot(A,B,color='Red')
[<matplotlib.lines.Line2D object at 0x000002E31AF522D0>]
>>> plt.show()
>>> #CAMBIO ESTREMI RETTA Ypre/Ytest=1
>>> A= np.array([-6,4])
>>> B= np.array([-6,4])
>>> plt.scatter(Ypred,Ytest)
<matplotlib.collections.PathCollection object at 0x000002E317732120>
>>> plt.plot(A,B,color='Red')
[<matplotlib.lines.Line2D object at 0x000002E31AFDE2D0>]
>>> plt.show()
>>> plt.show()
>>> plt.scatter(Ypred,Ytest)
<matplotlib.collections.PathCollection object at 0x000002E31B021D30>
>>> plt.plot(A,B,color='Red')
[<matplotlib.lines.Line2D object at 0x000002E319E46360>]
>>> plt.show()
>>> from sklearn.metrics import r2_score , mean_squared_error
>>> r2 = r2_score(Ytest,Ypred)
>>> r2
-1.2534013916111353
>>> EQM = mean_squared_error(Ytest,Ypred)
>>> EQM
10.696022446782338
>>> # SCALARE DATI PER RICALCOLARE R^2 & EQM
>>> from sklearn.preprocessing import StandardScaler
>>> scalare = StandardScaler()
>>> Xtrain_scal = scalare.fit_transform(Xtrain)
>>> Xtest_scal = scalare.transform(Xtest)
>>> modello_scal = LinearRegression()
>>> modello_scal.fit(Xtrain_scal,Ytrain)
LinearRegression()
>>> Ypred_scal = modello_scal.predict(Xtest_scal)
>>> r2_scal = r2_score(Ytest,Ypred_scal)
>>> r2_scal
-1.2534013916035458
>>> EQM_scal = mean_squared_error(Ytest,Ypred_scal)
>>> EQM_scal
10.696022446746312
