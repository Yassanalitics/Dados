#versão 2
import sys
import array

Array = array.array('i', [2, 4, 5, 6, 7, 8, 10, 11])

if len(sys.argv) < 2:
    sys.stdout.write("Use: python script.py <valor>\n")
    sys.exit(1)

n = int(sys.argv[1])  #n numnero procurado

if n in valores:
       sys.stdout.write("Encontrado.\n"
 else: 
      sys.stdout.write("Valor não encontrado.\n")

