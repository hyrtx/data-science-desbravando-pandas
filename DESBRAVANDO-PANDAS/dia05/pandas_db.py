# %%
import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine('sqlite:///../data/database.db')
engine

# %% Consultando tabela (Menos performático)
df_transactions_cart = pd.read_sql_table('transactions_cart', engine)
df_transactions_cart

# %% Rodando query (Mais performático)
query = "SELECT * FROM customers LIMIT 10"
df_customers = pd.read_sql_query(query, engine)
df_customers