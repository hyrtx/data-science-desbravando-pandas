
# %%
import pandas as pd

# %%
df: pd.DataFrame = pd.read_csv('../data/customers.csv', sep= ';')
df

# %% Ordenando pela pontuação
df.sort_values(by= 'Points', ascending= False)

# %% Ordenando por Pontuação Desc e Ordem Alfabetica Asc
df.sort_values(by= ['Points', 'Name'], ascending= [False, True])

# %% Maneira de transformar o dado feito em pipelines
nomes_colunas: dict = {
    'Name': 'nome',
    'Points': 'pontos'
}

df: pd.DataFrame = (df.sort_values(by= 'Points', ascending= False)
        .rename(columns= nomes_colunas))

df

# %% Remover linhas duplicadas
df.drop_duplicates()

# %% Remover linhas duplicadas a partir de colunas especificas
df.drop_duplicates(subset= ['Name', 'Points'])

# %% Remover linhas duplicadas definindo ordenação
df.drop_duplicates(subset= ['Name', 'Points'], keep='last')
