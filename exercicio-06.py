import sys
#A
"""def tam(arr):
    arranjo = 0
    try:
        while True:
            _ = arr[arranjo]
            arranjo += 1
    except IndexError:
        pass
    return arranjo

# Teste
arr = [4, 5, 8, 3, 6]
sys.stdout.write(f"tam(arr) é igual a {tam(arr)}\n")"""

#B
"""def tam(arr):
    c = 0
    try:
        while True:
            _ = arr[c]
            c += 1
    except IndexError:
        pass
    return c

def qtd_ad(arr, valor):
    try:
        i = 0
        while arr[i] != valor:
            i += 1
    except IndexError:
        sys.stdout.write("Valor não encontrado.\n")
        return
    sys.stdout.write(f"Possui {i} valores antes e {tam(arr)-i-1} valores depois do {valor}.\n")

arr = [4, 5, 8, 3, 6]
qtd_ad(arr, 3) """

#C
"""def tam(arr):
    c = 0
    try:
        while True:
            _ = arr[c]
            c += 1
    except IndexError:
        pass
    return c

def medio(arr):
    t = tam(arr)
    meio = (t - 1) // 2
    sys.stdout.write(f"Valor médio do arranjo: {arr[meio]}\n")

arr = [4, 5, 8, 3, 6]
medio(arr)"""
