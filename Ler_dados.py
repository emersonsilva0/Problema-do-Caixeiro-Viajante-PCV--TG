import pandas as pd

def ler_dados(nome_arquivo):
    # Lê o arquivo como um DataFrame do pandas e converte diretamente para uma matriz (lista de listas)
    return pd.read_csv(nome_arquivo, header=None, delim_whitespace=True).values.tolist()

# Bases de dados a ser usadas
bases_de_dados = ["ATT48", "DANTZIG42", "FRI26", "GR17", "P01"]

# Caminho dos arquivos 
caminho =  "C:\\Users\\Emersontntky\\TG\\Base de Dados\\"

# Coloca cada base de dados e armazenar as matrizes em um dicionário
matrizes = {nome_dos_dados:ler_dados(caminho + f'{nome_dos_dados.lower()}.txt') for nome_dos_dados in bases_de_dados}

# Imprimir as matrizes de cada base de dados
for nome_dos_dados, matriz in matrizes.items():
    print(f"Matriz da base de dados {nome_dos_dados}:")
    for linha in matriz:
        print(linha)
    print("\n")
