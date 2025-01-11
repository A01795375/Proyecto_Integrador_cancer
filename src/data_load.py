#### Obrtencion del dataset del repositorio chembl y guardar el dataset como CSV

import pandas as pd
from chembl_webresource_client.new_client import new_client
import locale
import sys
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import randn
from scipy.stats import mannwhitneyu

def data_retrival ():
    from chembl_webresource_client.new_client import new_client
    # Crear cliente para targets
    target_client = new_client.target   

    # Buscar objetivos que contengan "VEGF" en su nombre o descripción
    targets = target_client.filter(target_synonym__icontains='VEGF')
    print("Getting targets")    

    # Obtener los IDs de los objetivos
    target_ids = [target['target_chembl_id'] for target in targets] 

    # Crear cliente para bioactividad
    activity_client = new_client.activity   

    # Lista para almacenar los DataFrames individuales
    dataframes = []
  
    print("Selectging IC50")
    for target_id in target_ids:
        try:
            # Obtener actividades (incluyendo IC50) para cada objetivo relacionado con "VEGF"
            activities = activity_client.filter(target_chembl_id=target_id, standard_type="IC50")   

            if activities:
                # Convertir la respuesta en un DataFrame y agregar el ID del objetivo
                df_temp = pd.DataFrame.from_dict(activities)
                df_temp['target_chembl_id'] = target_id 

                # Añadir el DataFrame a la lista
                dataframes.append(df_temp)  

        except Exception as e:
               print(f'Error al procesar el objetivo {target_id}: {str(e)}')
   
    # Concatenar todos los DataFrames en uno solo
    print("conactenating frames")
    if dataframes:
        df_search = pd.concat(dataframes, ignore_index=True)
        #print(df_search)
    else:
        print("No se encontraron resultados.")
    
    return df_search

if __name__ == '__main__':
     
    output_data_set = sys.argv[1]
    df_search = data_retrival()
    pd.DataFrame(df_search).to_csv(output_data_set, index=False)
