# %%
import pandas as pd

# %%
data: dict = {
    'nome': ['Maria', 'João', 'Lara', 'Jorge'],
    'sobrenome': ['Ataide', 'Pereira', 'Silva', 'Ramos'],
    'idade': [31, 32, 31, 2]
}

# %%
data['idade'][0]

# %%
df = pd.DataFrame(data)
df

# %%
df['idade'].iloc[0]

# %%
df.iloc[0]

# %%
df.info(memory_usage= 'deep')

# %%
df.index

# %%
df.columns

# %%
df.index

# %%
df.dtypes

# %%
df.head(2)

# %%
df.tail(2)