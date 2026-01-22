"""
Funzioni di utilità per l'analisi dei segnali del giroscopio
"""
import numpy as np
import pandas as pd
from pathlib import Path


def load_gyro_data(file_path):
    """
    Carica i dati del giroscopio da file.
    
    Args:
        file_path: percorso del file gyro_exp*.txt
    
    Returns:
        DataFrame con colonne ['gyro_x', 'gyro_y', 'gyro_z']
    """
    data = np.loadtxt(file_path)
    df = pd.DataFrame(data, columns=['gyro_x', 'gyro_y', 'gyro_z'])
    return df


def load_labels():
    """
    Carica le etichette temporali.
    
    Returns:
        DataFrame con colonne ['exp_id', 'user_id', 'activity_id', 'start', 'end']
    """
    labels_path = Path(__file__).parent / 'RawData' / 'labels.txt'
    labels = pd.read_csv(labels_path, sep=' ', header=None,
                         names=['exp_id', 'user_id', 'activity_id', 'start', 'end'])
    return labels


def get_sampling_frequency():
    """Ritorna la frequenza di campionamento in Hz"""
    return 50.0
