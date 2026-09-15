from random import randint

def contar(matriz):
    n = len(matriz)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            cont = 0
            for k in range(n):
                if matriz[i][k] == 1 and matriz[j][k] == 1:
                    cont += 1
            total += cont * (cont - 1) // 2
    return total

# Preenchendo uma matriz com 0 e 1 (1° [] = linha, 2° [] = coluna)

matriz = [[randint(0, 1) for j in range(4)] for i in range(4)]

# Imprimindo a matriz com formato de matriz

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end='\t')
    print()
    print()

total = contar(matriz)
print(f'Total de subgrades = {total}')