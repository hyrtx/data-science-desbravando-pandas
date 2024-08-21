# %%
import pandas as pd

# %%
df_customers = pd.read_csv('../data/customers.csv', sep= ';')
df_customers

# %% Tamanho do Dataframe
df_customers.shape

# %% Uso da memória
df_customers.info(memory_usage= 'deep')

# %% Verificando tipos
df_customers.dtypes

# %% Descrevendo colunas
df_customers.describe()

# %% Adicionando valores de séries
df_customers['Points'] + 1000

# %% Reduzindo valores de séries
df_customers['Points'] - 1000

# %% Multiplicando valores de séries
df_customers['Points'] * 10

# %% Filtrando o dataset
condicao = df_customers['Points'] > 1000
df_customers[condicao]

# %% Filtrando o nome com mais pontos
condicao = df_customers['Points'] == df_customers['Points'].max()
nome_mais_pontos = df_customers[condicao]['Name'].iloc[0]
nome_mais_pontos

# %% filtrando pessoas entre 1000 e 2000 pontos
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao]['Name']

# %% Alterando df após filtro fazendo copy
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers_1000_2000 = df_customers[condicao].copy()
df_customers_1000_2000['Points'] = df_customers_1000_2000['Points'] + 1000
df_customers_1000_2000

# %% Acessando mais de uma coluna
df_customers[['UUID', 'Name']]

# %% Ordenando as colunas em ordem alfabetica
colunas = df_customers.columns.to_list()
colunas.sort()
df_customers[colunas]

# %% renomeando um dataframe

df_customers.rename(columns= {'Name': 'Nome', 'Points': 'Pontos'}, inplace= True)