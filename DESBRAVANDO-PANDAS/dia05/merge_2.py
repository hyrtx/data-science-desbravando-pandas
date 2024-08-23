# %%
import pandas as pd

# %%
df_customers = pd.read_csv('../data/customers.csv', sep= ';')
df_customers

# %%
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

# %%
df_transactions_parquet = pd.read_parquet('../data/transactions_cart.parquet')
df_transactions_parquet

# %% Fazendo merge com mais de uma tabela
df_join = (df_transactions.merge(df_customers,
                                how='inner',
                                left_on='IdCustomer',
                                right_on='UUID',
                                suffixes=['_trans', '_cust'])
                           .merge(df_transactions_parquet,
                                how='left',
                                left_on='UUID_trans',
                                right_on='IdTransaction'))