Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
DF= pd.read_csv(r'C:\Users\utente\Desktop\variazione_peso.csv', encoding='ISO-8859-1')
DF.info()
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
X= DF.iloc[:,9]
Y=DF.iloc[:,11]
>>> plt.scatter(X,Y)
<matplotlib.collections.PathCollection object at 0x0000022CFA473140>
>>> plt.show()
>>> coppie = list(zip(X,Y))
>>> coppie
[(45.36, 1.22), (45.36, -0.82), (45.36, -0.77), (48.67, -1.09), (51.44, 1.63), (51.94, -2.59), (52.84, -4.04), (55.75, 2.27), (56.74, 0.54), (58.83, -2.99), (61.96, 0.68), (62.23, -4.67), (62.64, 0.68), (62.78, 0.91), (63.68, 0.36), (64.18, 1.63), (64.77, 0.64), (65.73, -2.54), (66.0, 0.36), (66.18, -0.64), (66.81, 0.54), (67.72, 0.27), (68.58, -8.39), (68.67, -1.68), (69.35, -5.67), (69.81, 1.09), (69.99, -0.45), (70.53, 0.91), (70.81, -2.4), (71.08, -1.22), (71.44, 2.18), (71.8, -1.0), (71.89, -1.95), (73.8, 1.63), (73.84, -1.95), (74.03, -0.73), (74.21, -10.25), (75.02, 1.09), (75.11, 2.18), (75.21, 0.68), (76.02, 0.54), (76.25, -1.04), (76.75, 0.0), (76.79, 2.0), (76.88, -3.86), (76.97, -5.67), (77.07, -5.9), (77.07, 0.73), (77.29, -5.67), (77.97, -3.31), (78.2, -0.32), (78.56, 0.0), (78.61, 2.0), (79.11, 0.36), (79.56, -1.22), (81.56, 0.91), (81.78, 0.18), (81.96, 0.64), (82.24, -4.45), (82.24, -0.5), (82.46, 0.45), (82.51, 0.82), (82.51, 0.27), (82.74, -7.8), (82.78, -10.98), (82.92, 1.27), (83.33, -1.41), (83.69, -2.27), (83.91, 0.91), (84.01, 1.22), (84.46, -6.58), (86.0, -2.18), (86.32, 2.18), (86.86, 0.54), (87.0, 1.63), (88.22, -2.27), (88.68, 0.36), (88.77, -14.65), (88.9, 0.95), (88.99, -5.13), (89.63, 0.91), (89.72, 2.18), (90.17, -2.0), (90.22, -2.49), (91.63, 0.95), (92.03, -2.27), (92.12, 0.27), (93.03, -3.58), (93.67, 1.36), (93.89, 0.82), (94.3, -16.19), (94.8, -2.04), (96.62, 0.14), (97.25, 0.18), (97.25, 1.09), (102.6, -0.73), (103.42, 0.41), (103.6, 0.09), (106.5, -1.18), (108.05, -2.59)]
>>> inerzia = []
>>> for i in range (1,6):
...     kmeans = KMeans(n_clusters=i)
...     kmeans.fit(coppie)
...     inerzia.append(kmeans.inertia_)
... 
...     
KMeans(n_clusters=1)
KMeans(n_clusters=2)
KMeans(n_clusters=3)
KMeans(n_clusters=4)
KMeans(n_clusters=5)
>>> plt.plot(range(1,6) , inerzia)
[<matplotlib.lines.Line2D object at 0x0000022CFED4E210>]
>>> plt.title("Metodo a gomito")
Text(0.5, 1.0, 'Metodo a gomito')
>>> plt.xlabel("INERZIA")
Text(0.5, 0, 'INERZIA')
>>> plt.ylabel("CLUSTER")
Text(0, 0.5, 'CLUSTER')
>>> plt.show()
>>> kmeans = KMeans(n_clusters=4)
>>> kmeans.fit(coppie)
KMeans(n_clusters=4)
>>> plt.scatter(X,Y,c=kmeans.labels_)
<matplotlib.collections.PathCollection object at 0x0000022CFED4E6C0>
>>> plt.show()
