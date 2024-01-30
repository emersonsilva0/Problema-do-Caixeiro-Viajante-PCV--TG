import pandas as pd

def ler_arquivo_para_matriz(nome_arquivo):
    # Lê o arquivo como um DataFrame do pandas e converte diretamente para uma matriz (lista de listas)
    return pd.read_csv(nome_arquivo, header=None, delim_whitespace=True).values.tolist()

# Bases de dados a serem consideradas
bases_de_dados = ["ATT48", "DANTZIG42", "FRI26", "GR17", "P01"]

# Carregar cada base de dados e armazenar as matrizes em um dicionário
matrizes_bases = {base: ler_arquivo_para_matriz(f'{base.lower()}.txt') for base in bases_de_dados}

# Imprimir as matrizes de cada base de dados
for base, matriz in matrizes_bases.items():
    print(f"Matriz da base de dados {base}:")
    for linha in matriz:
        print(linha)
    print("\n")
