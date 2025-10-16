import sys
import array

numbers = array.array('i', [99, 85, 74, 52])

# Somar os quatro valores
total = sum(numbers)

# Exibir a soma usando sys.stdout
sys.stdout.write("A soma dos valores é: " + str(total) + "\n")

