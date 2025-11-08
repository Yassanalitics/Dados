#exemplo 2
import sys
number = int(sys.argv[1])
divisor = int(sys.argv[2])

if divisor > 0 and number > divisor:
    res = number / divisor
    sys.stdout.write("\nResultado: " + str(res))
else:
    sys.stdout.write("\nDivisão não permitida.")

#true false
