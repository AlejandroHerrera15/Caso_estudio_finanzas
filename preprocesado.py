import pandas as pd
import seaborn as sns
tabla_nuevos='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_nuevos_creditos.csv'
tabla_hist='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_historicos.csv'
tabla_nuevos=pd.read_csv(tabla_nuevos)
tabla_hist=pd.read_csv(tabla_hist)


sns.histplot(data=tabla_hist, x="NoPaidPerc")

tabla_hist.info()