# %%
import pandas as pd

# %%
df_products: pd.DataFrame = pd.read_csv('../data/products.csv',
                          sep=';', 
                          names= ['id', 'name', 'description'])
df_products

# %%
novos_nomes: dict = {
    'name': 'nome',
    'description': 'descricao'
}

df_products.rename(columns= novos_nomes, inplace= True)
df_products