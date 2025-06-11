import pandas as pd
from faker import Faker
import random

faker = Faker('pt-BR')
# caso queria em portugues -> feker = Faker('pt-BR)

def gerar_dados_brutos(num_registros):
    dados_brutos = []
    lista_cidade = set()
    
    while len(dados_brutos) < num_registros:
        nome_cidade = faker.estado()

        if nome_cidade not in lista_cidade:
            lista_cidade.add(nome_cidade)

            # gerar populacao aleatoria ente 10k e 5mi
            populacao = faker.random_int(min=10000, max=5000000)

            # taxa de homicidios entre 1.0 e 15.0 arredondado e com casa arredondado
            taxa_homicidios = round(random.uniform(1.0, 15.0),1)
            dados_brutos.append({
                "Cidade" : nome_cidade,
                "Populacao" : populacao,
                "Taxa homicidio" : taxa_homicidios
            })

    return pd.DataFrame(dados_brutos)


num_registros = 10
df = gerar_dados_brutos(num_registros)

print(df)

output_csv = "taxa_homicidios.csv"
df.to_csv(output_csv, index=False)