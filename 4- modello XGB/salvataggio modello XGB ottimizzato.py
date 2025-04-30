Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> DF= pd.read_csv(r'C:\Users\utente\Desktop\variazione_peso.csv', encoding='ISO-8859-1')
>>> DF.replace(["M", "F","Sedentario","Basso","Medio","Alto","Sufficiente","Bassa","Buona","Ottima"],[0,1,0.1,0.3,0.6,1,0.25,0.5,0.75,1],inplace=True)

Warning (from warnings module):
  File "<pyshell#2>", line 1
FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
>>> X=DF.iloc[:,[0,1,2,3,5,6,7,8,9]]
>>> y= DF.iloc[:,11]
>>> from sklearn.model_selection import train_test_split
>>> Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,test_size=0.25)
>>> import xgboost as xgb
>>> modelloXGB = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=50,learning_rate=0.1)
>>> modelloXGB.fit(Xtrain,Ytrain)
XGBRegressor(base_score=None, booster=None, callbacks=None,
             colsample_bylevel=None, colsample_bynode=None,
             colsample_bytree=None, device=None, early_stopping_rounds=None,
             enable_categorical=False, eval_metric=None, feature_types=None,
             feature_weights=None, gamma=None, grow_policy=None,
             importance_type=None, interaction_constraints=None,
             learning_rate=0.1, max_bin=None, max_cat_threshold=None,
             max_cat_to_onehot=None, max_delta_step=None, max_depth=None,
             max_leaves=None, min_child_weight=None, missing=nan,
             monotone_constraints=None, multi_strategy=None, n_estimators=50,
             n_jobs=None, num_parallel_tree=None, ...)
Ypred= modelloXGB.predict(Xtest)
from sklearn.metrics import r2_score, mean_squared_error
r2XGB= r2_score(Ytest,Ypred)
eqmXGB = mean_squared_error(Ytest,Ypred)
print ("r2:",r2XGB,"     ","errore qadratico medio:",eqmXGB)
r2: 0.5342190954628018       errore qadratico medio: 8.577937098771038
#TUNING PARAMETRI (SOFT)
from sklearn.model_selection import GridSearchCV
parametri = {'n_estimators':[50,100],'max_depth':[2,3],'learning_rate':[0.1,0.2]}
griglia= GridSearchCV( estimator= modelloXGB, param_grid= parametri, scoring= 'neg_mean_squared_error' , cv=2,verbose=1, n_jobs=1)
griglia.fit(Xtrain,Ytrain)
Fitting 2 folds for each of 8 candidates, totalling 16 fits
GridSearchCV(cv=2,
             estimator=XGBRegressor(base_score=None, booster=None,
                                    callbacks=None, colsample_bylevel=None,
                                    colsample_bynode=None,
                                    colsample_bytree=None, device=None,
                                    early_stopping_rounds=None,
                                    enable_categorical=False, eval_metric=None,
                                    feature_types=None, feature_weights=None,
                                    gamma=None, grow_policy=None,
                                    importance_type=None,
                                    interaction_constraints=None...
                                    max_cat_threshold=None,
                                    max_cat_to_onehot=None, max_delta_step=None,
                                    max_depth=None, max_leaves=None,
                                    min_child_weight=None, missing=nan,
                                    monotone_constraints=None,
                                    multi_strategy=None, n_estimators=50,
                                    n_jobs=None, num_parallel_tree=None, ...),
             n_jobs=1,
             param_grid={'learning_rate': [0.1, 0.2], 'max_depth': [2, 3],
                         'n_estimators': [50, 100]},
             scoring='neg_mean_squared_error', verbose=1)
ottimizzazione = griglia.best_params_
print(ottimizzazione)
{'learning_rate': 0.2, 'max_depth': 2, 'n_estimators': 50}
modelloXGB_ottimizzato= griglia.best_estimator_
Ypred_ottimizzato = modelloXGB_ottimizzato.predict(Xtest)
r2XGB_ottimizzato = r2_score(Ytest,Ypred_ottimizzato)
eqmXGB_ottimizzato = mean_squared_error(Ytest,Ypred_ottimizzato)
print ("r2 ottimizzato:",r2XGB_ottimizzato,"     ","errore qadratico medio ottimizzato:",eqmXGB_ottimizzato)
r2 ottimizzato: 0.8056072941991317       errore qadratico medio ottimizzato: 3.5799844660368283
import pickle
with open ("modello xgb ottimizzato.pkl","wb") as f:
    pickle.dump(modelloXGB_ottimizzato, f)

    
