import pandas as pd
from scipy.stats import shapiro

# Specifica il percorso del tuo file Excel
percorso_file_excel = './throughput.xlsx'

# Leggi il file Excel utilizzando pandas
dati = pd.read_excel(percorso_file_excel, header=None)

# Estrai i dati come vettore
vettore_dati = dati.iloc[:, 0].values

# Applica il test di normalità di Shapiro-Wilk
statistica, p_value = shapiro(vettore_dati)

# Stampa i risultati
print("Statistiche:", statistica)
print("Valore p:", p_value)