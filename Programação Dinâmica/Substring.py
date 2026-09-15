# Função para calcular o tamanho da maior subsequência
def calcular_tamanho(v1:str, v2: str) -> int:
    tabela = [[0 for j in range(len(v2) + 1)]for i in range(len(v1) + 1)]
    
    for i in range(1, len(v1) + 1):
        for j in range(1, len(v2) + 1):
            if v1[i - 1] == v2[j - 1]: # O verdadeiro valor começa em 0, então temos que fazer i - 1
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])
                
    return tabela, tabela[len(v1)][len(v2)]
            
# Função para imprimir a matriz
def imprimir(matriz):
    
    print(f'Matriz das palavras Linha = Palavra 1 / Coluna = Palavra 2')
    print()
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='\t')
        print()
    
# Função main
def main():
    v1 = input('Palavra um: ')
    v2 = input('Palavra dois: ')
    print()
    
    matriz, valor = calcular_tamanho(v1, v2)
    impressao = imprimir(matriz)
    total = valor 
    
    print()
    print(f'Tamanho da maior subsequência = {total}')

# Programa principal
if __name__ == '__main__':
    main()