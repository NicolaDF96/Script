import os
import pandas as pd

# Cartella contenente i file .pcap
folder = "./handshake"

# Creazione di un DataFrame vuoto per i risultati
results = []

# Ciclo per attraversare tutti i file .pcap nella cartella
for file in os.listdir(folder):
    if file.endswith(".pcap") and file.startswith("client"):
        # Esegue il comando tshark e salva l'output in un file di testo
        os.system(f"tshark -z conv,udp -r {folder}/{file} -q > output.txt")

        # Esegue il comando tail, head, tr e awk per estrarre le informazioni desiderate dall'output
        result = os.popen("tail -2 output.txt | head -1 | tr -s ' ' | awk -F ' ' '{print $5 \",\" $14}'").read().strip()

        # Aggiunge il risultato alla lista dei risultati
        results.append({"File": file, "Risultato": result})

# Creazione del DataFrame dai risultati
results_df = pd.DataFrame(results)

# Salvataggio del DataFrame in un file Excel
results_df.to_excel("risultati.xlsx", index=False)

# Leggi il file Excel
df = pd.read_excel('risultati.xlsx')

# Crea una nuova colonna chiamata "Throughput"
df['Throughput'] = ""

# Itera sulle righe del DataFrame
for index, row in df.iterrows():
    # Ottieni il valore dalla colonna "Risultato"
    risultato = row['Risultato']

    # Dividi i valori separati da virgola
    valori = risultato.split(',')
    value1 = float(valori[0])
    value2 = float(valori[1])
    result = (value1 / value2) * 8

    # Aggiorna il valore nella colonna "Throughput"
    df.at[index, 'Throughput'] = result

# Salva il DataFrame nel file Excel "throughput.xlsx"
df.to_excel('throughput.xlsx', index=False)