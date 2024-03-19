import pandas as pd
import heapq
import time
import networkx as nx
import matplotlib.pyplot as plt

# Função para ler os dados de um arquivo
def ler_dados(nome_arquivo):
    return pd.read_csv(nome_arquivo, header=None, sep='\s+').values.tolist()

# Algoritmo de Prim para encontrar a Árvore Geradora Mínima
def prim(grafo, inicio):
    nos_abertos = []  # Lista de nós abertos para exploração
    nos_fechados = []  # Lista de nós já visitados

    pesos = []  # Lista de pesos das arestas
    predecessores = []  # Lista de predecessores dos nós
    for n in grafo.nodes:
        pesos.append(float('inf'))  # Inicializar os pesos como infinito
        predecessores.append(None)  # Inicializar os predecessores como nulos

    pesos[inicio] = 0  # Definir o peso do nó inicial como 0
    nos_abertos.append(inicio)  # Adicionar o nó inicial à lista de nós abertos
    
    # Enquanto houver nós abertos para explorar
    while len(nos_abertos) != 0:
        # Escolher o nó com o menor peso
        n = min(nos_abertos, key=lambda x: pesos[x])
        nos_abertos.remove(n)  # Remover o nó escolhido da lista de nós abertos
        nos_fechados.append(n)  # Adicionar o nó escolhido à lista de nós fechados

        # Percorrer os vizinhos do nó escolhido
        for vizinho in grafo.neighbors(n):
            # Verificar se o vizinho não foi visitado e se o peso é menor do que o peso atual
            if vizinho not in nos_fechados and pesos[vizinho] > grafo.edges[n, vizinho]['weight']: 
                nos_abertos.append(vizinho)  # Adicionar o vizinho à lista de nós abertos
                predecessores[vizinho] = n  # Atualizar o predecessor do vizinho
                pesos[vizinho] = grafo.edges[n, vizinho]['weight']  # Atualizar o peso do vizinho

    return predecessores, pesos  # Retornar array de predecessores e pesos

# Nomes das bases de dados
bases_de_dados = ["ATT48", "DANTZIG42", "FRI26", "GR17", "P01"]

# Caminho para os arquivos de dados
caminho =  "C:\\Users\\Emersontntky\\TG\\Base de Dados\\"

# Carregar as matrizes de dados dos arquivos
matrizes = {nome_dos_dados:ler_dados(caminho + f'{nome_dos_dados.lower()}.txt') for nome_dos_dados in bases_de_dados}

# Iniciar o cronômetro
inicio = time.time()

# Iterar sobre as matrizes de dados
for nome_dos_dados, matriz in matrizes.items():
    # Verificar limite de tempo
    if time.time() - inicio > 12*60*60:
        print("Limite de tempo atingido.")
        break
    
    print(f"Matriz da base de dados {nome_dos_dados}:")
    
    # Criar um grafo
    grafo = nx.Graph()
    
    # Adicionar arestas ao grafo
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                grafo.add_edge(i, j, weight=matriz[i][j])
    
    # Encontrar a Árvore Geradora Mínima usando o algoritmo de Prim
    predecessores, pesos = prim(grafo, 0)
    
    # Criar um novo grafo para a Árvore Geradora Mínima
    agm = nx.Graph()
    for i in range(len(predecessores)):
        if predecessores[i] is not None:
            agm.add_edge(i, predecessores[i], weight=pesos[i])
    
    # Imprimir o peso total da Árvore Geradora Mínima e o número de arestas
    print(f"Peso total da árvore geradora mínima: {sum(pesos)}")
    print(f"Número de arestas na árvore geradora mínima: {agm.number_of_edges()}")

    # Desenhar o grafo
    pos = nx.spring_layout(agm)
    nx.draw_networkx_nodes(agm, pos, node_size=300, node_color='r')
    nx.draw_networkx_edges(agm, pos, edgelist=agm.edges())
    nx.draw_networkx_labels(agm, pos, font_size=10)
    plt.axis('off')
    plt.show()
    print("\n")
