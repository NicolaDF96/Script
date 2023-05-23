# pip install pandas
# pip install openpyxl

import pandas as pd
from scipy.stats import shapiro
import math
import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt

aioquic = []
picoquic = []
quiche = []
ngtpc2 = []
lsquic=[]

def leggi_file_excel(nome_file):
    try:
        dati = pd.read_excel(nome_file)
        array_dati = dati.values.tolist()
        return array_dati
    except FileNotFoundError:
        print(f"Il file '{nome_file}' non è stato trovato.")
        return []
    except Exception as e:
        print("Si è verificato un errore durante la lettura del file.")
        print(e)
        return []

# Specifico nome file excel
nome_file_excel = "Throughput553.xlsx"  # Percorso del file Excel

#Carico i dati nell'array
dati_array = leggi_file_excel(nome_file_excel)

# Stampo l'array dei dati caricati in precedenza
for riga in dati_array:
    aioquic.append(riga[0])
    picoquic.append(riga[1])
    quiche.append(riga[2])
    ngtpc2.append(riga[3])
    lsquic.append(riga[4])

plt.hist(aioquic, edgecolor='black', bins=20)
plt.savefig("aioquic.png")
plt.figure().clear()

plt.hist(picoquic, edgecolor='black', bins=20)
plt.savefig("picoquic.png")
plt.figure().clear()

plt.hist(quiche, edgecolor='black', bins=20)
plt.savefig("quiche.png")
plt.figure().clear()

plt.hist(ngtpc2, edgecolor='black', bins=20)
plt.savefig("ngtpc2.png")
plt.figure().clear()


plt.hist(lsquic, edgecolor='black', bins=20)
plt.savefig("lsquic.png")
plt.figure().clear()
