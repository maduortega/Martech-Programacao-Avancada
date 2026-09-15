# Função de programação dinamica
def mochila(itens: list[dict], capacidade: int) -> tuple[int, list]: 
    n = len(itens) # Pega a quantidade de itens
    tabela = [[0 for j in range(capacidade + 1)]for i in range(n + 1)] # Na linha temos os itens e na coluna temos a capacidade
    
    for i in range(1, n + 1):
        peso = itens[i - 1]["Peso"] # Ou .get('Peso') --> (melhor)
        valor = itens[i - 1].get('Preço')
        for j in range(1, capacidade + 1):
            anterior = tabela[i - 1][j]
            item_com_valor = -1
            
            if peso <= j:
                item_com_valor = valor + tabela[i - 1][j - peso] # Se tenho uma mochila de 4kg
                                                            # e estou inserindo 2kg, ainda sobram 2kg
            tabela[i][j] = max(anterior, item_com_valor)
            
    valor_max = tabela[n][capacidade] # Os valores estão na última linha/coluna
    escolhidos = []
    
    for i in range(n, 0, -1): # Pegando valores de trás para frente
        if tabela[i][capacidade] != tabela[i - 1][capacidade]:
            escolhidos.append(itens[i - 1].get('Nome'))
            capacidade -= itens[i - 1].get('Peso')
    
    return valor_max, escolhidos

# Função main
def main():
    itens = [{'Nome': 'Rádio', 'Preço': 3000, 'Peso': 4},
        {'Nome': 'Notebook', 'Preço': 2000, 'Peso': 3},
    {'Nome': 'Violão', 'Preço': 1500, 'Peso': 1}
    ]
    
    capacidade = 4
    
    max, escolhidos = mochila(itens, capacidade)
    print(max)
    print(escolhidos)

# Programa principal
if __name__ == '__main__':
    main()