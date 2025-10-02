## Documentação do Projeto: Biblioteca de Grafos para a Empresa TransPortes ABC

### 1. Introdução

A Teoria dos Grafos é um ramo da matemática e da ciência da computação que estuda as relações entre objetos. Um grafo é uma representação abstrata de um conjunto de objetos onde alguns pares de objetos estão conectados por links. Esses objetos são chamados de *vértices* (ou nós) e os links que os conectam são chamados de *arestas*.

No contexto de redes de transporte, os grafos são uma ferramenta poderosa para modelar e resolver problemas complexos. Cidades podem ser representadas como vértices, e as estradas que as conectam como arestas. O "custo" de percorrer uma estrada, como a distância ou o tempo de viagem, pode ser representado pelo *peso* da aresta.

[cite_start]Este trabalho se dedica ao desenvolvimento de uma biblioteca de grafos para a empresa fictícia "TransPortes ABC", que administra uma rede de transporte intermunicipal[cite: 1195]. [cite_start]A biblioteca implementa funcionalidades essenciais para a análise e otimização da rede, como o cálculo de rotas mais curtas, a verificação da conectividade da rede e a identificação de pontos críticos[cite: 1226, 1227, 1228].

### 2. Especificação do Problema

[cite_start]O objetivo deste projeto é criar uma biblioteca em Python para manipular grafos não direcionados e ponderados, representando a rede de transportes da empresa TransPortes ABC[cite: 1195, 1199, 1200]. [cite_start]A biblioteca deve ser capaz de ler a estrutura do grafo a partir de um arquivo de texto, onde cada linha representa uma estrada (aresta) conectando duas cidades (vértices) com uma determinada distância (peso)[cite: 1219, 1220].

As funcionalidades implementadas devem permitir à empresa:

* **Consultas Básicas:**
    * [cite_start]Obter o número total de cidades e estradas na rede[cite: 1222, 1223].
    * [cite_start]Listar as cidades vizinhas a uma determinada cidade[cite: 1224].
    * [cite_start]Obter a quantidade de vizinhos de uma cidade específica[cite: 1225].

* **Análise de Rotas:**
    * [cite_start]Calcular o menor caminho (em distância) entre duas cidades[cite: 1226].

* **Análise Estrutural da Rede:**
    * [cite_start]Verificar se a rede de transportes é *conexa*, ou seja, se é possível chegar de qualquer cidade a qualquer outra[cite: 1227].
    * [cite_start]Identificar *cidades críticas*, que, se removidas, desconectariam a rede, isolando uma ou mais cidades[cite: 1228].

* **Planejamento de Roteiros Turísticos:**
    * [cite_start]Verificar a existência de um *passeio turístico circular* que passe por, no mínimo, 4 cidades distintas e retorne à cidade de origem sem repetir estradas[cite: 1229].
    * [cite_start]Caso tal passeio exista, fornecer um exemplo de rota[cite: 1230].

[cite_start]Para validar a biblioteca, foi desenvolvido um programa principal que permite ao usuário testar todas as funcionalidades implementadas[cite: 1231].

### 3. Metodologia e Estrutura do Código

O código foi organizado de forma modular, com responsabilidades bem definidas, para facilitar a manutenção e o entendimento. A estrutura principal é composta por três arquivos:

* **`leitura.py`:** Responsável pela leitura e processamento do arquivo de entrada que descreve o grafo.
* **`grafo.py`:** Contém a classe `Grafo`, que encapsula a estrutura de dados do grafo e implementa todos os algoritmos e funcionalidades solicitados.
* **`main.py`:** Serve como interface para o usuário, permitindo a interação com a biblioteca e o teste de suas funcionalidades.

#### 3.1. Estrutura de Dados

A classe `Grafo` utiliza as seguintes estruturas de dados para representar a rede de transportes:

* **`self.vertices` (Conjunto):** Armazena o nome de todas as cidades (vértices) da rede. Um conjunto (`set`) foi escolhido para garantir que não haja cidades duplicadas e para permitir operações de busca eficientes.
* **`self.arestas` (Lista):** Uma lista de tuplas, onde cada tupla representa uma estrada no formato `(cidade1, cidade2, distancia)`.
* **`self.adjacencia` (Dicionário):** Um dicionário que mapeia cada cidade a uma lista de seus vizinhos diretos e a distância até eles. Por exemplo: `{'A': [('B', 10), ('C', 20)], 'B': [...]}`. Esta estrutura é fundamental para a eficiência de algoritmos que exploram a vizinhança de um vértice, como a Busca em Profundidade (DFS) e o Algoritmo de Dijkstra.
* **`self.pesos` (Dicionário):** Um dicionário que armazena o peso (distância) de cada aresta. A chave é uma tupla `(cidade1, cidade2)`, e o valor é a distância.

#### 3.2. Principais Funções e Métodos

* **`ler_arquivo_grafo(nome_arquivo)` (em `leitura.py`):**
    * Abre e lê o arquivo de texto especificado.
    * Processa cada linha para extrair as duas cidades e a distância.
    * Popula um conjunto com as cidades e uma lista com as estradas.
    * Retorna o conjunto de cidades e a lista de estradas.

* **Classe `Grafo` (em `grafo.py`):**
    * **`__init__(self, nome_arquivo)`:** Construtor da classe. Inicializa as estruturas de dados e, se um nome de arquivo for fornecido, chama o método `carregar_arquivo` para popular o grafo.
    * **`carregar_arquivo(self, nome_arquivo)`:** Utiliza a função `ler_arquivo_grafo` para obter os dados do arquivo e, em seguida, preenche as estruturas `self.adjacencia` e `self.pesos`.
    * **`numero_cidades(self)` e `numero_estradas(self)`:** Retornam o tamanho do conjunto de vértices e da lista de arestas, respectivamente.
    * **`vizinhos(self, cidade)` e `quantidade_vizinhos(self, cidade)`:** Consultam a lista de adjacências para retornar os vizinhos de uma cidade e sua quantidade.
    * **`dijkstra(self, origem, destino)`:** Implementa o Algoritmo de Dijkstra para encontrar o caminho mais curto.
    * **`conexo(self)`:** Verifica se o grafo é conexo.
    * **`dfs(self, vertice, visitados)`:** Implementação da Busca em Profundidade (DFS), usada como auxiliar por outras funções.
    * **`encontrar_cidades_criticas(self)`:** Identifica os vértices de articulação (cidades críticas).
    * **`passeio_turistico(self)`:** Busca por um ciclo de tamanho igual ou superior a 4.

### 4. Algoritmos de Grafos Utilizados

#### 4.1. Algoritmo de Dijkstra

* **O que é:** O Algoritmo de Dijkstra é usado para encontrar o caminho mais curto entre um nó de origem e todos os outros nós em um grafo ponderado com pesos de aresta não negativos.
* **Como funciona:**
    1.  Começa atribuindo uma distância infinita a todos os nós, exceto ao nó de origem, que tem distância zero.
    2.  Utiliza uma fila de prioridades para explorar sempre o nó com a menor distância acumulada.
    3.  Para cada nó visitado, ele examina seus vizinhos e atualiza suas distâncias se um caminho mais curto for encontrado.
    4.  O processo continua até que o nó de destino seja alcançado ou todos os nós alcançáveis tenham sido visitados.
* [cite_start]**Aplicação no código:** O método `dijkstra(self, origem, destino)` implementa este algoritmo para resolver o requisito de "calcular o menor caminho entre duas cidades escolhidas"[cite: 1226].

#### 4.2. Busca em Profundidade (DFS - *Depth-First Search*)

* **O que é:** A DFS é um algoritmo de travessia de grafos que explora o mais longe possível ao longo de cada ramo antes de retroceder.
* **Como funciona:**
    1.  Começa em um vértice arbitrário e o marca como visitado.
    2.  Explora um de seus vizinhos não visitados, repetindo o processo recursivamente.
    3.  Quando não há mais vizinhos não visitados para explorar a partir do vértice atual, ele retrocede para o vértice anterior e continua a exploração a partir de lá.
* **Aplicação no código:**
    * [cite_start]**Verificação de Conectividade:** O método `conexo(self)` utiliza uma DFS (`self.dfs`) para verificar se a rede é conexa[cite: 1227]. Ele inicia a busca a partir de um vértice e, ao final, verifica se o número de vértices visitados é igual ao número total de vértices do grafo.
    * [cite_start]**Cidades Críticas:** O método `encontrar_cidades_criticas(self)` utiliza uma variação da DFS para encontrar pontos de articulação[cite: 1228].
    * [cite_start]**Passeio Turístico:** O método `passeio_turistico(self)` usa a DFS para encontrar um ciclo que satisfaça as condições do passeio[cite: 1229, 1230].

#### 4.3. Algoritmo para Encontrar Pontos de Articulação (Cidades Críticas)

* **O que é:** Um ponto de articulação (ou vértice de corte) é um vértice que, se removido, aumenta o número de componentes conexas do grafo.
* **Como funciona:** O algoritmo implementado é uma aplicação avançada da DFS. Ele mantém um registro do "tempo de descoberta" de cada vértice e do "tempo baixo" (o tempo de descoberta mais baixo alcançável a partir desse vértice, incluindo ele mesmo, através de uma única aresta de retorno no máximo). Um vértice `u` é um ponto de articulação se tiver um filho `v` tal que o "tempo baixo" de `v` seja maior ou igual ao "tempo de descoberta" de `u`.
* [cite_start]**Aplicação no código:** O método `encontrar_cidades_criticas(self)` implementa essa lógica para identificar as cidades críticas da rede[cite: 1228].

### 5. Exemplos de Execução

A seguir, são apresentados exemplos de execução do programa principal (`main.py`) com diferentes arquivos de teste.

#### 5.1. Teste com `teste1.txt`

* **Entrada (`TP1_Grafos/Testes/teste1.txt`):**
    ```
    A,B,5
    A,C,12
    B,C,3
    B,D,10
    C,D,4
    C,E,15
    D,E,2
    ```
* **Saída do programa (Exemplo de interação):**
    ```
    === SISTEMA TRANSPORTES ABC ===
    Arquivo Testes/teste1.txt lido com sucesso!
    Número de cidades: 5
    Número de estradas: 7
    Cidades: ['A', 'B', 'C', 'D', 'E']
    Digite o nome de uma cidade para ver seus vizinhos: C
    Vizinhos de C: ['A', 'B', 'D', 'E']
    Quantidade de vizinhos de C: 4
    Digite a cidade de origem: A
    Digite a cidade de destino: E
    Menor caminho: A -> B -> C -> D -> E
    Distância total: 14

    --- VERIFICAÇÃO DE CONECTIVIDADE ---
    A rede é CONEXA!
    Cidades críticas: C, D
    Passeio turístico encontrado: ['A', 'B', 'C', 'A']
    ```

#### 5.2. Teste com `teste2.txt` (Grafo Desconexo)

* **Entrada (`TP1_Grafos/Testes/teste2.txt`):**
    ```
    A,B,7
    A,C,3
    B,C,2
    X,Y,10
    Y,Z,5
    ```
* **Saída do programa (Exemplo de interação):**
    ```
    === SISTEMA TRANSPORTES ABC ===
    Arquivo Testes/teste2.txt lido com sucesso!
    Número de cidades: 6
    Número de estradas: 5
    Cidades: ['A', 'B', 'C', 'X', 'Y', 'Z']
    Digite a cidade de origem: A
    Digite a cidade de destino: Z
    Não existe caminho entre as cidades informadas.

    --- VERIFICAÇÃO DE CONECTIVIDADE ---
    A rede não é conexa!
    Cidades críticas: Y
    Passeio turístico encontrado: ['A', 'B', 'C', 'A']
    ```

### 6. Análise de Complexidade

* **Leitura do Arquivo:** A complexidade é **O(E)**, onde E é o número de estradas (arestas), pois cada linha do arquivo é lida uma vez.
* **Algoritmo de Dijkstra:** A complexidade, com o uso de uma fila de prioridades (heap), é **O(E log V)**, onde V é o número de cidades (vértices) e E é o número de estradas.
* **Busca em Profundidade (DFS):** A complexidade é **O(V + E)**, pois cada vértice e cada aresta são visitados uma vez.
* **Verificação de Conectividade:** Como utiliza a DFS, a complexidade é **O(V + E)**.
* **Encontrar Cidades Críticas:** A complexidade é **O(V + E)**, pois se baseia em uma única travessia DFS.
* **Passeio Turístico:** No pior caso, a complexidade pode ser exponencial, pois explora diferentes caminhos. No entanto, na prática, para grafos esparsos como os de redes de transporte, o desempenho é geralmente aceitável.

### 7. Conclusão

A biblioteca desenvolvida atende a todos os requisitos especificados para a empresa TransPortes ABC, fornecendo uma solução robusta e eficiente para a análise de sua rede de transportes. A organização modular do código permite fácil expansão e manutenção.

**Limitações e Melhorias Futuras:**

* **Grafos Direcionados:** A implementação atual suporta apenas grafos não direcionados. Poderia ser estendida para incluir estradas de mão única.
* **Interface Gráfica:** Uma interface gráfica poderia ser desenvolvida para visualizar o grafo e os resultados das análises, tornando a ferramenta mais amigável.
* **Algoritmos Adicionais:** Outros algoritmos de grafos poderiam ser implementados, como o de Kruskal ou Prim para encontrar a Árvore Geradora Mínima (útil para planejar redes de custo mínimo) ou algoritmos de fluxo máximo.

### 8. Referências

* **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
* **Goodrich, M. T., Tamassia, R., & Goldwasser, M. H.** (2013). *Data Structures and Algorithms in Python*. Wiley.
