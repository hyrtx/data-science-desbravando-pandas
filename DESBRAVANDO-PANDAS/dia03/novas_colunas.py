# %%
import pandas as pd
import numpy as np

# %% Carregando Dados
df = pd.read_csv('../data/customers.csv', sep= ';')
df

# %% Criando coluna nova a partir de outra
df['Points_double'] = df['Points'] * 2
df

# %% Criando uma coluna nova a partir de duas colunas
df['Points_ratio'] = df['Points_double'] / df['Points']
df

# %% Coluna a partir de escalar
df['Constante'] = 1
df

# %% Utilizando métodos matemáticos
df['Points_log'] = np.log(df['Points'])
df

# %% Invocando str para deixar o nome maiúsculo
df['Upper_name'] = df['Name'].str.upper()
df

# %% Criando funções
def get_first(nome: str):
    return nome.split('_')[0]

# No caso do apply, não invocamos a função
df['First_name'] = df['Name'].apply(get_first)
df

# %% Usando função lambda
df['First_name'] = df['Name'].apply(lambda x: x.split('_')[0])

# %% Criando colunas com condicionais

def intervalo_faixa(ponto: int) -> str:
    if ponto < 1000:
        return 'Baixo'
    elif ponto < 2500:
        return 'Médio'
    else:
        return 'Alto'
    
df['Faixa_pontos'] = df['Points'].apply(intervalo_faixa)
df

# %% Criando colunas com condicionais em mais de uma coluna

data = {
    'nome': ['Will', 'Phil', 'Ashley', 'Vivian'],
    'recencia': [1, 30, 10, 45],
    'valor': [100, 2000, 15, 500],
    'frequencia': [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)
df_crm

# %%
def rfv(row):

    nota = 0

    if row['recencia'] <= 10:
        nota += 10
    elif row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota +=0
    
    if row['valor'] > 1000:
        nota += 10
    elif row['valor'] > 100:
        nota += 5
    else:
        nota +=0

    if row['frequencia'] > 10:
        nota += 10
    elif row['frequencia'] > 5:
        nota += 5
    else:
        nota +=0

    return nota

df_crm['nota_rfv'] = df_crm.apply(rfv, axis= 1)
df_crm