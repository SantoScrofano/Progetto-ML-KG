Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> DF = pd.read_csv(r'C:\Users\utente\Desktop\variazione_peso.csv', encoding='ISO-8859-1')
>>> DF.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 12 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   ETA'                      100 non-null    int64  
 1   SESSO                     100 non-null    object 
 2   CALORIE ASSUNTE           100 non-null    float64
 3   CALORIE BRUCIATE(RIPOSO)  100 non-null    float64
 4   SURPLUS CALORICO          100 non-null    float64
 5   SETTIMANE VARIAZIONE      100 non-null    int64  
 6   LIVELLO ALLENAMENTO       100 non-null    object 
 7   QUALITA' SONNO            100 non-null    object 
 8   LIVELLO STRESS            100 non-null    int64  
 9   PESO INIZIALE             100 non-null    float64
 10  PESO FINALE               100 non-null    float64
 11  VARIAZIONE PESO           100 non-null    float64
dtypes: float64(6), int64(3), object(3)
memory usage: 9.5+ KB
>>> DF1= DF.iloc[:,0:4]
>>> DF2= DF.iloc[:,4:8]
>>> DF3= DF.iloc[:,8:]
>>> DF1.describe()
             ETA'  CALORIE ASSUNTE  CALORIE BRUCIATE(RIPOSO)
count  100.000000       100.000000                100.000000
mean    37.910000      3518.292000               2518.206000
std     12.219454       513.313097                364.431221
min     18.000000      2030.900000               1566.500000
25%     26.750000      3233.300000               2255.050000
50%     38.000000      3636.050000               2519.500000
75%     46.250000      4000.000000               2805.975000
max     59.000000      4000.000000               3390.800000
>>> DF2.describe()
       SURPLUS CALORICO  SETTIMANE VARIAZIONE
count        100.000000            100.000000
mean        1000.091000              6.920000
std          371.560827              3.515277
min           82.500000              1.000000
25%          766.950000              4.000000
50%         1013.100000              7.000000
75%         1253.325000             10.000000
max         1922.500000             12.000000
DF3.describe()
       LIVELLO STRESS  PESO INIZIALE  PESO FINALE  VARIAZIONE PESO 
count      100.000000     100.000000   100.000000        100.000000
mean         4.810000      77.805800    76.543900         -1.262700
std          2.576879      13.759239    13.874885          3.377448
min          1.000000      45.360000    44.540000        -16.190000
25%          2.750000      69.695000    67.832500         -2.270000
50%          5.000000      78.085000    77.020000          0.045000
75%          7.000000      87.305000    85.412500          0.842500
max          9.000000     108.050000   105.460000          2.270000
# CODIFICA ONE HOT
MODASESSO= pd.get_dummies(DF.iloc[:,1])
MODALIVELLO_ALLENAMENTO = pd.get_dummies(DF.iloc[:,6])
MODAQUALITA_SONNO = pd.get_dummies(DF.iloc[:,7])
print(MODASESSO,MODALIVELLO_ALLENAMENTO,MODAQUALITA_SONNO)
        F      M
0   False   True
1    True  False
2    True  False
3   False   True
4    True  False
..    ...    ...
95  False   True
96   True  False
97  False   True
98  False   True
99  False   True

[100 rows x 2 columns]      Alto  Basso  Medio  Sedentario
0   False   True  False       False
1   False  False  False        True
2   False   True  False       False
3   False  False   True       False
4   False  False   True       False
..    ...    ...    ...         ...
95  False  False   True       False
96  False  False   True       False
97  False  False  False        True
98  False   True  False       False
99  False  False   True       False

[100 rows x 4 columns]     Bassa  Buona  Ottima  Sufficiente
0   False   True   False        False
1    True  False   False        False
2   False   True   False        False
3    True  False   False        False
4   False  False   False         True
..    ...    ...     ...          ...
95  False   True   False        False
96  False  False    True        False
97  False  False    True        False
98   True  False   False        False
99   True  False   False        False

[100 rows x 4 columns]
# METODO .map
mappaturasesso= {"F":3, "M":5}
mappaturalivello_allenamento= {"Sedentario":10 , "Basso":20 , "Medio":30, "Alto":40 }
mappaturaqualita_sonno= {"Sufficiente":25 , "Bassa":50 , "Buona":75, "Ottima":100 }
SESSO_NUMERO= DF.iloc[:,1].map(mappaturasesso)
ALLENAMENTO_NUMERO= DF.iloc[:,6].map(mappaturalivello_allenamento)
SONNO_NUMERO = DF.iloc[:,7].map(mappaturaqualita_sonno)
print ( SESSO_NUMERO , ALLENAMENTO_NUMERO , SONNO_NUMERO)
0     5
1     3
2     3
3     5
4     3
     ..
95    5
96    3
97    5
98    5
99    5
Name: SESSO, Length: 100, dtype: int64 0     20
1     10
2     20
3     30
4     30
      ..
95    30
96    30
97    10
98    20
99    30
Name: LIVELLO ALLENAMENTO, Length: 100, dtype: int64 0      75
1      50
2      75
3      50
4      25
     ... 
95     75
96    100
97    100
98     50
99     50
Name: QUALITA' SONNO, Length: 100, dtype: int64
from scipy import stats
MODAdelSESSO= stats.mode(SESSO_NUMERO)
MODAdellALLENAMENTO= stats.mode(ALLENAMENTO_NUMERO)
MODAdelSONNO= stats.mode(SONNO_NUMERO)
print(MODAdelSESSO)
ModeResult(mode=5, count=57)
print(MODAdellALLENAMENTO)
ModeResult(mode=20, count=31)
print(MODAdelSONNO)
ModeResult(mode=50, count=38)
# MODA = {sesso:'Maschi' | livello_allenamento:'basso' | qualità_sonno:'bassa'}
