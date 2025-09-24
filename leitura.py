def ler_arquivo_grafo(nome_arquivo):
    cidades = set()
    estradas = []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arq:
            for linha in arq:
                linha_limpa = linha.strip()

                if linha_limpa:
                    partes = linha_limpa.split(',')

                    if len(partes) == 3:
                        cidade1 = partes[0]
                        cidade2 = partes[1]
                        distancia = int(partes[2].strip())
                        
                        cidades.add(cidade1)
                        cidades.add(cidade2)
                        estradas.append((cidade1, cidade2, distancia))
                    else:
                        print("Linha não está feita corretamente")
        
        
        print(f"Arquivo {nome_arquivo} lido com sucesso!")
        return cidades, estradas
        
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado")
        return set(), []
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return set(), []