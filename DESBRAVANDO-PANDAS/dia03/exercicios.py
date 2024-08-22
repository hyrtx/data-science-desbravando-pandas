# %%
import pandas as pd

'''
1. Qual é o valor da última transação de cada IdCustomer?
'''

# %% Importando os dados
df = pd.read_excel('../data/transactions.xlsx')
df

# %% Ordenando e dropando duplicatas
df_last_transactions = (df.sort_values(by= 'DtTransaction', ascending= False)
        .drop_duplicates(subset=['IdCustomer']))

df_last_transactions

# %% Verificando os valores únicos no df
df['IdCustomer'].nunique()

# %% Validando se a transação aparente é a última
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]
