# Analisi dei Segnali del Giroscopio


## Dataset
Dati del giroscopio da smartphone per il riconoscimento di attività umane e transizioni posturali.



**Fonte:** [UCI Machine Learning Repository - Smartphone-based recognition of human activities and postural transitions](https://archive.ics.uci.edu/dataset/341/smartphone+based+recognition+of+human+activities+and+postural+transitions)

I dati utilizzati in questo lavoro provengono dal dataset "Smartphone-Based Recognition of Human Activities and Postural Transitions" di Jorge Reyes-Ortiz, Davide Anguita, Luca Oneto, Xavier Parra, disponibile sul UCI Machine Learning Repository e rilasciato sotto licenza CC BY 4.0.

**Utenti**: 10 (user01 - user10)  
**Frequenza di campionamento**: 50 Hz  
**Sensore**: Giroscopio triassiale (x, y, z)

## Struttura
- `RawData/`: File dei segnali grezzi del giroscopio
  - `gyro_exp*.txt`: Dati giroscopio (3 colonne: gyro_x, gyro_y, gyro_z)
  - `labels.txt`: Etichette temporali (exp_id, user_id, activity_id, start, end)



## Riferimenti Teorici
Questa relazione integra la teoria vista a lezione con l'analisi pratica dei dati. Gli argomenti coperti sono:

- **Tipi di segnali** (analogici, digitali)
- **Sistemi e risposta all’impulso**
- **Sistemi LTI**
- **Trasformata di Fourier (DTFT, DFT)**
- **Trasformata Z**
- **Conversione AD/DA**
- **Analisi spettrale**
- **Processi random**
- **DSP analogico e digitale**
