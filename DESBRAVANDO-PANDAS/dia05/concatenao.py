# %%
import pandas as pd
import os

def import_etl(path: str) -> pd.DataFrame:

    name: str = path.split('/')[-1].split('.')[0]

    df: pd.DataFrame = (pd.read_csv(path, sep= ';')
                          .rename(columns={'valor': name})
                          .set_index(['cod', 'nome', 'período']))
    
    return df

# %%
path: str = '../data/ipea/'
files = os.listdir(path)

dfs = []
for i in files: