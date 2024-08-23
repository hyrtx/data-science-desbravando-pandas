# %%
import pandas as pd

# %%
data_01 = {
    'id': [1, 2, 3, 4],
    'nome': ['Will', 'Phil', 'Ashley', 'Vivian'],
    'idade': [17, 47, 13, 46]
}

df_01 = pd.DataFrame(data_01)
df_01
# %%

data_02 = {
    'id': [5, 6, 7, 8],
    'nome': ['Hillary', 'Geoffrey', 'Jazz', 'Carlton'],
    'idade': [23, 49, 18, 17]
}

df_02 = pd.DataFrame(data_02)
df_02

# %%
data_03 = {
    'sobrenome': ['Smith', 'Banks', 'Banks', 'Banks'],
    'renda': [3100, 3100, 3200, 3200]
}

df_03 = pd.DataFrame(data_03)
df_03

# %% Empilhando as bases (Concat é concatenado pelo Index)

pd.concat([df_01, df_02]).reset_index(drop=True)

# %% Empilhando as bases de maneira lateral

pd.concat([df_01, df_03], axis= 1).reset_index(drop=True)