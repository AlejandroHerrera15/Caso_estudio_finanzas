import pandas as pd
import seaborn as sns
tabla_nuevos='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_nuevos_creditos.csv'
tabla_hist='https://raw.githubusercontent.com/juancamiloespana/LEA3_FIN/main/data/datos_historicos.csv'
tabla_nuevos=pd.read_csv(tabla_nuevos)
tabla_hist=pd.read_csv(tabla_hist)


sns.histplot(data=tabla_hist, x="NoPaidPerc")

tabla_hist.info()
tabla_hist.drop(columns=['ID','HomeOwnership', 'Education', 'MaritalStatus'],inplace=True)

from matplotlib.pyplot import figure
figure(figsize=(20,6))
sns.heatmap(tabla_hist.corr(),cmap = sns.cubehelix_palette(as_cmap=True), annot = True, fmt = ".2f")


tabla_hist['prob_calculada']=(tabla_hist['DebtRatio']*tabla_hist['NoPaidPerc'])*100
tabla_hist['prob_calculada'].describe()








