from leitura import ler_arquivo_grafo
import sys


class Grafo:
    def __init__(self, nome_arquivo=None):
        self.vertices = set()
        self.arestas = []
        self.adjacencia = {}
        self.pesos = {}
        if nome_arquivo:
            self.carregar_arquivo(nome_arquivo)

    def numero_cidades(self):
        return len(self.vertices)

    def numero_estradas(self):
        return len(self.arestas)

    def vizinhos(self, cidadeAtual):
        return [vizinho for vizinho, _ in self.adjacencia.get(cidadeAtual, [])]

    def quantidade_vizinhos(self, cidadeAtual):
        return len(self.vizinhos(cidadeAtual))

    def carregar_arquivo(self, nome_arquivo):

        cidadeAtuals, estradas = ler_arquivo_grafo(nome_arquivo)

        if not cidadeAtuals:
            print("Não foi possível carregar o grafo.")
            return False

        self.vertices = cidadeAtuals
        self.arestas = estradas

        self.adjacencia = {}  # Lista de vizinhos
        self.pesos = {}

        for cidadeAtual1, cidadeAtual2, distancia in estradas:
            if cidadeAtual1 not in self.adjacencia:
                self.adjacencia[cidadeAtual1] = []
            if cidadeAtual2 not in self.adjacencia:
                self.adjacencia[cidadeAtual2] = []

            self.adjacencia[cidadeAtual1].append((cidadeAtual2, distancia))
            self.adjacencia[cidadeAtual2].append((cidadeAtual1, distancia))

            self.pesos[(cidadeAtual1, cidadeAtual2)] = distancia
            self.pesos[(cidadeAtual2, cidadeAtual1)] = distancia

        return True

    def listar_cidades(self):
        return sorted(list(self.vertices))

    def listar_estradas(self):
        return self.arestas

    def dijkstra(self, origem, destino):
        import heapq

        distancias = {v: sys.maxsize for v in self.vertices}
        anteriores = {v: None for v in self.vertices}
        distancias[origem] = 0

        fila = [(0, origem)]

        while fila:
            distancia_atual, atual = heapq.heappop(fila)

            if atual == destino:
                break

            for vizinho, peso in self.adjacencia.get(atual, []):
                nova_distancia = distancia_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        # Reconstrução do caminho
        caminho = []
        atual = destino
        while atual:
            caminho.append(atual)
            atual = anteriores[atual]
        caminho.reverse()

        if distancias[destino] == sys.maxsize:
            return None, sys.maxsize  # Caminho não encontrado

        return caminho, distancias[destino]

    def conexo(self):  # será usado busca em profundidade para saber se o grafo é conexo
        vertice_inicial = next(iter(self.vertices))
        visitados = set()
        self.dfs(vertice_inicial, visitados)
        return len(visitados) == len(self.vertices)

    def dfs(self, vertice, visitados):
        visitados.add(vertice)
        for vizinho, _ in self.adjacencia.get(vertice, []):
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def encontrar_cidades_criticas(self):
        visitado = {v: False for v in self.vertices}
        tempo_descoberta = {v: float('inf') for v in self.vertices}
        tempo_baixo = {v: float('inf') for v in self.vertices}
        pais = {v: None for v in self.vertices}
        cidadeAtuals_criticas = set()
        self.contador_tempo = 0

        def dsf_cidadeAtual_critica(u):
            visitado[u] = True
            self.contador_tempo += 1
            tempo_descoberta[u] = tempo_baixo[u] = self.contador_tempo
            filhos = 0

            for v, _ in self.adjacencia.get(u, []):
                if not visitado[v]:
                    filhos += 1
                    pais[v] = u
                    dsf_cidadeAtual_critica(v)
                    tempo_baixo[u] = min(tempo_baixo[u], tempo_baixo[v])
                    if pais[u] is None and filhos > 1:
                        cidadeAtuals_criticas.add(u)
                    if pais[u] is not None and tempo_baixo[v] >= tempo_descoberta[u]:
                        cidadeAtuals_criticas.add(u)
                elif v != pais[u]:
                    tempo_baixo[u] = min(tempo_baixo[u], tempo_descoberta[v])
        for i in self.vertices:
            if not visitado[i]:
                dsf_cidadeAtual_critica(i)
        return cidadeAtuals_criticas

    def passeio_turistico(self):

        def dfs(cidade_atual, origem, visitados, caminho, profundidade):
            visitados.add(cidade_atual)
            caminho.append(cidade_atual)
            for vizinho, _ in self.adjacencia.get(cidade_atual, []):
                if vizinho == origem and profundidade >= 4:
                    return caminho.copy()
                if vizinho not in visitados:
                    resultado = dfs(vizinho, origem, visitados,
                                    caminho, profundidade + 1)
                    if resultado:
                        return resultado
            caminho.pop()
            visitados.remove(cidade_atual)
            return None

        for cidade in self.vertices:
            visitados = set()
            caminho = []
            resultado = dfs(cidade, cidade, visitados, caminho, 1)
            if resultado:
                return True, resultado
        return False, None
