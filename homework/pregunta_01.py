"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_csv(r'files/input/solicitudes_de_credito.csv',sep=';', index_col=0)


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """



    df_clean = df.copy()
    #df_clean = df_clean.apply(lambda x: x.str.lower().str.strip() if(x.dtype=='object') else x)
    df_clean.sexo = df_clean.sexo.astype('category')
    df_clean.sexo = df_clean.sexo.str.lower()
    df_clean["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df_clean["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))
    df_clean.monto_del_credito = df_clean.monto_del_credito.str.strip().str.replace("$","").str.replace(",","").str.replace(".00","")
    df_clean.monto_del_credito = df_clean.monto_del_credito.astype(int)
    #df_clean = df_clean.apply(lambda x: x.str.replace("_"," ") if(x.dtype=='object') else x)
    #df_clean = df_clean.apply(lambda x: x.str.replace("-"," ") if(x.dtype=='object') else x)
    df_clean.barrio = df_clean.barrio.str.lower().str.replace("_"," ").str.replace("-"," ")
    df_clean.idea_negocio = df_clean.idea_negocio.str.lower().str.replace("_"," ").str.replace("-"," ").str.strip()
    df_clean.línea_credito = df_clean.línea_credito.str.lower().str.replace("_"," ").str.replace("-"," ").str.strip()
    df_clean.tipo_de_emprendimiento = df_clean.tipo_de_emprendimiento.str.lower().str.replace("_"," ").str.replace("-"," ").str.strip()
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.dropna()

    os.makedirs('files/output/',exist_ok=True)
    df_clean.to_csv(r'files/output/solicitudes_de_credito.csv', sep=';',index=True)
    return df_clean




pregunta_01()