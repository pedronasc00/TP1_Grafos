cidades = set()
estradas = []
try:
    with open('Testes/teste1.txt', 'r', encoding='utf-8') as arq:
        for linha in arq:
            linha_limpa = linha.strip()

            if linha_limpa:
                partes = linha_limpa.split(',')

                if len(partes) == 3:
                    cidade1 = partes[0]
                    cidade2 = partes[1]
                    distancia = partes[2]

                    cidades.add(cidade1)
                    cidades.add(cidade2)

                    estradas.append((cidade1, cidade2, distancia))
                else:
                    print("Linha não está feita corretamente")
except FileNotFoundError:
    print("Arquivo para teste não foi encontrado")

print("Cidades (Vértices) do arquivo:")
cidades_ordenadas = sorted(list(cidades))
print(cidades_ordenadas)
print(f"Numero de cidades encontradas: {len(cidades)}")

print("\nEstradas (Arestas) encontradas:")
for estrada in estradas:
    print(f"De {estrada[0]} para {estrada[1]} tem distância de {estrada[2]} km")
print(f"Total de estrada: {len(estradas)}")