# %%
import pandas as pd

# %%
df_customers = pd.read_csv('../data/customers.csv', sep= ';')
df_customers

# %%
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

# %% Fazendo merge com todas as colunas
df_transactions.merge(df_customers, how='left', on='UUID')