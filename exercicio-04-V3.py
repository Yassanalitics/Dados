#versão3
import sys
import array

valores = array.array('i', [2, 4, 5, 6, 7, 8, 10, 11])
n = 7  
if n in valores:
    pos = valores.index(n)
    sys.stdout.write(f"Encontrado na posição {pos}\n")
else:
    sys.stdout.write("Valor não encontrado\n")
