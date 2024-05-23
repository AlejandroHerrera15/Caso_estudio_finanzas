import pandas as pd
import seaborn as sns
from matplotlib.pyplot import figure

url_nuevos='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_nuevos_creditos.csv'
url_hist='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_historicos.csv'

df_nuevos=pd.read_csv(url_nuevos)
df_hist=pd.read_csv(url_hist)

### Exploración inicial
df_nuevos.info()
df_nuevos.duplicated().sum()
df_nuevos.isnull().sum()
df_nuevos.shape


df_hist.info()
df_hist.duplicated().sum()
df_hist.isnull().sum()
df_hist.shape

#Las bases de nuevos usuarios e historicos no cuentan con datos duplicados ni nulos.


### Variable objetivo
sns.histplot(data=df_hist, x="NoPaidPerc")


### Correlación numéricas
df_hist_num = df_hist.select_dtypes(include=['number'])
figure(figsize=(20,6))
sns.heatmap(df_hist_num.corr(),cmap = sns.cubehelix_palette(as_cmap=True), annot = True, fmt = ".2f")













