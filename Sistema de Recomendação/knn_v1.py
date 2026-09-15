from math import sqrt

###############################################################
dados = [
    ('u1', 3, 4, 4, 1, 4),
    ('u2', 4, 3, 5, 1, 5),
    ('u3', 2, 5, 1, 3, 1)
]

genero = ['comedia', 'acao', 'drama', 'terror', 'romance']
###############################################################

# Função para calcular a distância entre dois usuários
def calcular_dist(usuario: tuple, novo_u: tuple) -> float:
    soma = 0
    for i in range(1, len(usuario)):
        c1 = usuario[i] # Primeiro valor do usuário de indice i
        c2 = novo_u[i] # Primeiro valor do novo usuário (indice i)
        
        if c1 is not None and c2 is not None:
            soma += (c1 - c2) ** 2
    return sqrt(soma)

# Função para encontrar o vizinho mais próximo
def mais_proximo(dados: list[tuple], novo_u: tuple) -> tuple:
    melhor_vizi = None
    melhor_dist = None
    
    for usuario in dados:
        dist = calcular_dist(usuario, novo_u)
        if (melhor_dist is None) or (dist < melhor_dist):
            melhor_dist = dist # Retornando a tupla inteira
            melhor_vizi = usuario # Retornando a tupla inteira
    return melhor_vizi, melhor_dist

# Função para fazer a recomendação
def recomendar(dados: list[tuple], novo_u: tuple) -> tuple:
    vizinho, d_vizinho = mais_proximo(dados, novo_u)
    if vizinho is None or d_vizinho == float('inf'):
        return novo_u, d_vizinho
    
    selminina = [None] * len(novo_u) # Selmininha seria a indicação
    for i in range(len(novo_u)): # Começa no 1, pq o índice 0 é o nome do usuário
        if novo_u[i] is not None:
            selminina[i] = novo_u[i]
        else:
            selminina[i] = vizinho[i]
    
    return tuple(selminina), vizinho, d_vizinho

# Função principal
def main():
    novo_u = ('ut', 5, 4, 2, 1, None)

    indicacao, vizinho, d_vizinho = recomendar(dados, novo_u)
    print(f'Vizinho mais próximo: {vizinho}')
    print(f'Indicação: {indicacao}')
    print(f'Distância até o vizinho mais próximo: {d_vizinho:.2f}')

if __name__ == '__main__':
    main()