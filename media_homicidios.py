import pandas as pd
import numpy as np
from scipy.stats import trim_mean

def get_medias(df_dados_brutos):
    media_populacao = df_dados_brutos['Populacao'].mean()
    media_homicidio = df_dados_brutos['Taxa homicidio'].mean()

    proporca_corte = 0.1
    media_aparada_populacao = trim_mean(df_dados_brutos['Populacao'], proportiontocut=proporca_corte)
    media_aparada_homicidio = trim_mean(df_dados_brutos['Taxa homicidio'], proportiontocut=proporca_corte)

    mediana_populacao = df_dados_brutos['Populacao'].median()
    mediana_homicidios = df_dados_brutos['Taxa homicidio'].median()

    media_poderada = np.average(df_dados_brutos['Taxa homicidio'], weights=df_dados_brutos['Populacao'])

    
    
    df_medias = df_dados_brutos = pd.DataFrame({
        'Populacao' :[media_populacao , media_aparada_populacao, mediana_populacao, np.nan],
        'Taxa homicidio' :[media_homicidio, media_aparada_homicidio, mediana_homicidios, media_poderada]
    }, index = ['Media', 'media Aparada', 'mediana', 'media poderada'])

    return df_medias




df_dados_brutos = pd.read_csv('taxa_homicidios.csv')
print(df_dados_brutos)
df_medias = get_medias(df_dados_brutos)
print(df_medias.to_string(float_format="%.2f"))