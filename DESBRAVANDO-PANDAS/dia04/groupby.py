# %%
import pandas as pd
import datetime as dt

# %%
df = pd.read_excel('../data/transactions.xlsx')
df

# %% Uma agregação: Soma pontos por usuário

df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()

# %% Multiplas agregações
(df.groupby(['IdCustomer'])
   .agg({
       'Points': 'sum',
       'UUID': 'count',
       'DtTransaction': 'max'
       })
  .rename(columns= {
       'Points': 'Valor',
       'UUID': 'Frequencia',
       'DtTransaction': 'Ultima_Data'
       })
   .reset_index())

# %% Agregando de maneira personalizada
def recencia(x):
    diff = dt.datetime.now() - x.max()
    return diff.days

(df.groupby(['IdCustomer'])
   .agg({
       'Points': 'sum',
       'UUID': 'count',
       'DtTransaction': recencia
       })
  .rename(columns= {
       'Points': 'Valor',
       'UUID': 'Frequencia',
       'DtTransaction': 'Recencia'
       })
   .reset_index())