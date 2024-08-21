# %%
import pandas as pd

# %% Importando excel
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

# %% Qtd de linhas e colunas
df_transactions.shape

# %% Verificando df
df_transactions.head()

# %% Alterando ordem das colunas
colunas = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']

df_transactions = df_transactions[colunas]
df_transactions

# %% Verificando memória
df_transactions.info(memory_usage= 'deep')
