#versão básica 
import sys
import array

Array = array.array('i', [2, 4, 5, 6, 7, 8, 10, 11])
n = 7
if n in Array:
    sys.stdout.write("Valor encontrado: " + str(n) + "\n")
else:
    sys.stdout.write("Valor não encontrado no arranjo.\n")

