import random
ponto = list[float]

# Função que calcula a distância entre dois pontos
def distancia(a: ponto, b: ponto):
    pass

# Função para calcular a média de cada cluster
def calcular_media(x : list[ponto]) -> ponto | None:
    pass

def kmeans(dados: list[ponto], k: int = 3, max_iter: int = 200, tolerancia: float = 1e-6): # Se eu não passar valor ele assume que esses valores devem ser considerados
    n = len(dados) # Tamanho da lista
    dimensao = len(dados[0]) # 2 elementos dentro de casa listinha | Número de elementos em cada lista

    indices = list(range(n)) # Lista em um intervalo que vai de 0 até n - 1
    random.shuffle(indices) # Shuffle = sacudir, troca os valores de lugar
    
    centros = [dados[indices[i]][:] for i in range(k)] # [:] É um copy
    cluster = [-1] * n
    
    it = 0
    while it <= max_iter:
        it += 1
        for i in range(n):
            dado = dados[i] # Pega o primeiro ponto
            menor_distancia = float('inf')
            index = -1 # Índice invalido
            for j in range(k):
                dist = distancia(dado, centros[j])
                if dist < menor_distancia:
                    menor_distancia = dist
                    index = j
            if cluster[i] != index:
                cluster[i] = index
        
        # Reconstrução dos centros (centróides)        
        centro_aux : list[list[ponto]] = [[] for _ in range(k)] # k = cluster
        for i in range(n):
            centro_aux[cluster[i]].append(dados[i])
        
        novo_centro : list[ponto] = []
        # Calcula a média de cada um dos clusters auxiliares
        for i in range(k):
            media = calcular_media(centro_aux[i])
            if media is None:
                media = dados[random.randint(0, n)[:]]
            novo_centro.append(media)
            
        # Atribui os novos centros para a variável centro
        centro = novo_centro
    return centro, cluster

def main():
    dados = [ [1.0, 1.0], [1.2, 0.9], [0.9, 1.1], # Grupo A
            [4.0, 4.2], [3.9, 3.5], [4.1, 3.8], # Grupo B
          [8.0, 8.0], [8.3, 7.9], [7.7, 8.2] # Grupo C
    ]
    
    centro, cluster = kmeans(dados, k = 3, max_iter = 200, tolerancia = 1e-6) # 10 elevado a -6
    print('Centros')
    for i, c in enumerate(centro): # Enumera os centros (i = 1, c = valor 1° centro)
        print(f'c{i + 1} --> {c}')
        
    print()
    print('Label')
    for i, (dado, label) in enumerate(zip(dados, cluster)):
        print(f'{i + 1} --> {dado} --> cluster{label}')

if __name__ == '__main__':
    main()