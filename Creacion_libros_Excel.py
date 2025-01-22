import os
import pandas as pd

# TABLAS DE HECHO
# Crear una lista de todos los archivos CSV en el directorio
hechos_csv = [archivo for archivo in os.listdir('./TP_2/Database/Tablas_de_hecho') if archivo.endswith('.csv')]

# Crear un ExcelWriter para guardar los archivos CSV como un archivo de Excel
with pd.ExcelWriter("./TP_2/Database/Tablas_de_hecho.xlsx", engine="openpyxl") as writer:
    for archivo_csv in hechos_csv:
        # Cargar el CSV en un DataFrame
        df = pd.read_csv(os.path.join('./TP_2/Database/Tablas_de_hecho', archivo_csv))
        
        # Escribir el DataFrame en una hoja de Excel, usando el nombre del archivo CSV (sin la extensión) como nombre de la hoja
        nombre_hoja = os.path.splitext(archivo_csv)[0]  # Nombre de la hoja será el nombre del archivo sin la extensión
        df.to_excel(writer, index=False, sheet_name=nombre_hoja)

# TABLAS DE DIMENSION
dimensiones_csv = [archivo for archivo in os.listdir('./TP_2/Database/Tablas_de_dimension') if archivo.endswith('.csv')]

with pd.ExcelWriter("./TP_2/Database/Tablas_de_dimension.xlsx", engine="openpyxl") as writer:
    for archivo_csv in dimensiones_csv:
        df = pd.read_csv(os.path.join('./TP_2/Database/Tablas_de_dimension', archivo_csv))
        nombre_hoja = os.path.splitext(archivo_csv)[0]  
        df.to_excel(writer, index=False, sheet_name=nombre_hoja)