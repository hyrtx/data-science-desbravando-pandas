# %%
import pandas as pd
import numpy as np

# %%

data = {
    'nome': ['Will', 'Phil', 'Ashley', 'Vivian', 'Carlton'],
    'idade': [17, 47, 13, 46, np.nan],
    'renda': [np.nan, 12432, np.nan, 8365, 357],
}

df = pd.DataFrame(data)

# %% Verificando quantidade de NA de uma coluna
df['idade'].isna().sum()

# %% Verificando quantidade de NA de um df
df.isna().sum()

# %% Proporção de NAs
df.isna().mean()

# %% Preencher null com média (poderia ser com escalar)
df.fillna({
    'idade': df['idade'].mean(),
    'renda': df['renda'].mean()
})

# %% Como remover NAs (Remove linha inteira)
df.dropna()

# %% Como remover NAs se apenas todas as linhas forem NA
df.dropna(how= 'all')

# %% Como remover NAs por linhas especificas
df.dropna(subset= ['idade', 'renda'], how='any')

# %% Remover colunas que tenham NA
df.dropna(axis= 1, how='any')



