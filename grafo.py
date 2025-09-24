from leitura import ler_arquivo_grafo
import sys

class Grafo:
    def __init__ (self, nome_arquivo=None):
        self.vertices = set()
        self.arestas=[]
        self.adjacencia = {}
        self.pesos = {}
        if nome_arquivo:
            self.carregar_arquivo(nome_arquivo)

    def numero_cidades(self):
        return len(self.vertices)    
    def numero_estradas(self):
        return len(self.arestas)
    def vizinhos(self, cidade):
        return [vizinho for vizinho, _ in self.adjacencia.get(cidade, [])]
    def quantidade_vizinhos(self, cidade):
        return len(self.vizinhos(cidade))
    
    def carregar_arquivo(self, nome_arquivo):
        
        cidades, estradas = ler_arquivo_grafo(nome_arquivo)
        
        if not cidades:
            print("Não foi possível carregar o grafo.")
            return False
        
        self.vertices = cidades
        self.arestas = estradas
        
        self.adjacencia = {} #Lista de vizinhos
        self.pesos = {}
        
        for cidade1, cidade2, distancia in estradas:
            if cidade1 not in self.adjacencia:
                self.adjacencia[cidade1] = []
            if cidade2 not in self.adjacencia:
                self.adjacencia[cidade2] = []
                
            self.adjacencia[cidade1].append((cidade2, distancia))
            self.adjacencia[cidade2].append((cidade1, distancia))
            
            self.pesos[(cidade1, cidade2)] = distancia
            self.pesos[(cidade2, cidade1)] = distancia
        
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
    
    def conexo(self): #será usado busca em profundidade para saber se o grafo é conexo
        vertice_inicial=next(iter(self.vertices))
        visitados=set()
        self.dfs(vertice_inicial, visitados)
        return len(visitados)==len(self.vertices)
    def dfs(self, vertice, visitados):
        visitados.add(vertice)
        for vizinho, _ in self.adjacencia.get(vertice, []):
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)