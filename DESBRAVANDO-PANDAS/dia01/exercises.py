# %%
import pandas as pd

# %%
'''
01. Converta a seguinte lista de dados para uma Series Pandas e obtenha:
Média
Desvio Padrão
Máximo Valor

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
'''

def medidas_estatisticas(lista_dados: list) -> dict:
    medidas: dict = {}
    series_dados: pd.Series = pd.Series(lista_dados)

    # Média
    medidas['media'] = series_dados.mean()

    # Desvio Padrão
    medidas['desvio padrão'] = series_dados.std()

    # Máximo
    medidas['máximo'] = series_dados.max()

    return medidas

dados: list = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
medidas: dict = medidas_estatisticas(dados)

for k, v in medidas.items():
    print(f"{k}: {v}")

# %%
'''
02. Converta o seguinte dicionário para DataFrame e obtenha:
Sumário de cada coluna
Média da coluna idade
Último nome da coluna nome

dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}

'''

dados: dict = {
    'nome':['Téo', 'Nah', 'Napoleão'], 
    'idade': [31, 32, 14]
    }

df: pd.DataFrame = pd.DataFrame(dados)
print(df)

# Sumário de cada coluna
sumario: list = df.columns.values

# Media coluna idade
media_idade: float = df['idade'].mean()

# Último nome da coluna nome
ultimo_nome: str = df['nome'].iloc[-1]

# Printando resultados
print(sumario)
print(media_idade)
print(ultimo_nome)

