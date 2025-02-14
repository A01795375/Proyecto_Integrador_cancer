import pandas as pd
import numpy as np
import seaborn as sns
import re

def clean_seq (seq):
    aa_pfeature = ['A','C','D','E','F','G','H','I','K','L','M','N','P',
              'Q','R','S','T','V','W','Y']
    filtered_df = pd.DataFrame(seq)
    # 1. Poner en mayúsculas todos los aminoácidos de las secuencias
    filtered_df = filtered_df[0].str.upper()
    # 2. Identificar los péptidos con valores de X
    aa_x = filtered_df[filtered_df.apply(lambda x: 'X' in x)]
    # 3. Conservar solo los péptidos que contengan los aminoácidos para pfeatures
    filtered_df = filtered_df[filtered_df.apply(lambda x: all(char in aa_pfeature for char in x))]
    inicio_x = aa_x[aa_x.str.startswith('X')]
    # Función para quitar los caracteres 'x' al inicio de la secuencia
    aa_x = aa_x.apply(quitar_x_inicio)
    # Función para quitar los caracteres 'x' al final de la secuencia
    fin_x = aa_x[aa_x.str.endswith('X')].copy()
    aa_x = aa_x.apply(quitar_x_final)
    # Elimina los péptidos con X intermedia
    aa_x = aa_x[aa_x.apply(lambda x: all(char in aa_pfeature for char in x))]
    filtered_df = pd.concat([filtered_df, aa_x], ignore_index=True)
    return filtered_df
    
def quitar_x_inicio(secuencia):
        return re.sub(r'^X+', '', secuencia)

    # Finalizan con X
    
    

def quitar_x_final(secuencia):
        return re.sub(r'X+$', '', secuencia)
    # Aplicar la función a la columna 'Sequence'



    
    

