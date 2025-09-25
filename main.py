from grafo import Grafo

def verificar_conectividade_detalhada(grafo):
        print("\n--- VERIFICAÇÃO DE CONECTIVIDADE ---")
        
        if grafo.conexo():
            print("A rede é CONEXA!")
        else:
            print("A rede não é conexa!")
            
def main():
    print("=== SISTEMA TRANSPORTES ABC ===")
    
   
    grafo = Grafo("Testes/teste1.txt")  
    
    
    print(f"Número de cidades: {grafo.numero_cidades()}")
    print(f"Número de estradas: {grafo.numero_estradas()}")
    print(f"Cidades: {grafo.listar_cidades()}")
    
   
    cidade_escolhida = input("Digite o nome de uma cidade para ver seus vizinhos: ")
    if cidade_escolhida in grafo.vertices:
        vizinhos = grafo.vizinhos(cidade_escolhida)
        quantidade_vizinhos = grafo.quantidade_vizinhos(cidade_escolhida)
        print(f"Vizinhos de {cidade_escolhida}: {vizinhos}")
        print(f"Quantidade de vizinhos de {cidade_escolhida}: {quantidade_vizinhos}")
    else:
        print("Cidade não encontrada no grafo.")

    # Testar Dijkstra
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    
    caminho, distancia = grafo.dijkstra(origem, destino)
    if caminho:
        print(f"Menor caminho: {' -> '.join(caminho)}")
        print(f"Distância total: {distancia}")
    else:
        print("Não existe caminho entre as cidades informadas.")    

    #Testar conectividade
    verificar_conectividade_detalhada(grafo)
            
    #Testar cidades_criticas
    cidades_criticas = grafo.encontrar_cidades_criticas()
    if cidades_criticas:
        print(f"Cidades críticas: {', '.join(cidades_criticas)}")
    else:
        print("Não há cidades críticas na rede.")
            
       
if __name__ == "__main__":
    main()