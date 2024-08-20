# %%
import pandas as pd


# %%
idades = [30, 42, 90, 34]
media = sum(idades) / len(idades)

# %% 
# Transformação para séries Pandas
series_idades = pd.Series(idades)

# %%
# Métodos Pandas
# Média
series_idades.mean()

# %%
# Variância
series_idades.var()

# %%
# Desvio Padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# Percentil
series_idades.quantile(0.75)

# %%
# Dimensão da Série
series_idades.shape