import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


url_nuevos='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_nuevos_creditos.csv'
url_hist='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_historicos.csv'

df_nuevos=pd.read_csv(url_nuevos)
df_hist=pd.read_csv(url_hist)


### Modelo regresión lineal

