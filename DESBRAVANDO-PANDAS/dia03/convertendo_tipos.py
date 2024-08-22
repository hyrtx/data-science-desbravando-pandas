# %% 
import pandas as pd

# %% Carregando o Dataframe
df = pd.read_csv('../data/customers.csv', sep= ';')
df

# %% Verificando os tipos de cada variável
df.dtypes

# %% Convertendo tipos
df['Points'].astype(str)

# %% Convertendo mais de um tipo
df['Points_double'] = df['Points'] * 2
df[['Points', 'Points_double']].astype(str)