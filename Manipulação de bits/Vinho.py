import random

def descobrir(n: int, poison: int) -> int:
    k = n.bit_length() # Total de bits que representam o número que está em n
    cobaias = [0] * k
    for i in range(k):
        if poison & (1 << i) != 0:
            cobaias[i] = 1
            
    # Converter
    resultado = 0
    for i in range(k):
        if cobaias[i] == 1:
            resultado += 1 << i
        
    return resultado

# Programa principal
n = 8
poison = random.randint(0, n - 1)
resultado = descobrir(n, poison)
print(f'Garrafa Envenenada: {poison}')
print(f'Garrafa Envenenada Descobeta: {resultado}')