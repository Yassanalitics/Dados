import sys
#versão básica 
"""def soma():
    a = 8
    b = 5
    resultado = a + b
    sys.stdout.write(f"Soma: {a} + {b} = {resultado}\n")
    
def sub():
    a = 8
    b = 5
    resultado = a - b
    sys.stdout.write(f"Subtração: {a} - {b} = {resultado}\n")

def mul():
    a = 8
    b = 5
    resultado = a * b
    sys.stdout.write(f"Multiplicação: {a} * {b} = {resultado}\n")

def div_inteiro_resto():
    a = 8
    b = 5
    if b == 0:
        sys.stdout.write("Erro: Divisão por zero não é permitida.\n")
        return
    quociente = a // b
    resto = a % b
    sys.stdout.write(f"Divisão inteira: {a} // {b} = {quociente}\n")
    sys.stdout.write(f"Resto: {a} % {b} = {resto}\n")

#  Execução
sys.stdout.write(" Cálculos Básicos \n")
soma()
sub()
mul()
div_inteiro_resto()
"""
#Versão 1
"""def soma(a, b):
    sys.stdout.write(f"Soma: {a + b}\n")

def sub(a, b):
    sys.stdout.write(f"Subtração: {a - b}\n")

def mul(a, b):
    sys.stdout.write(f"Multiplicação: {a * b}\n")

def div_inteiro_resto(a, b):
    if b == 0:
        sys.stdout.write("Erro: divisão por zero\n")
    else:
        sys.stdout.write(f"Divisão inteira: {a // b}\n")
        sys.stdout.write(f"Resto: {a % b}\n")
      
a = int(sys.argv[1])
b = int(sys.argv[2])

soma(a, b)
sub(a, b)
mul(a, b)
div_inteiro_resto(a, b)"""

#versão 2 
"""def soma(a, b):
    sys.stdout.write(f"Soma: {a + b}\n")

def sub(a, b):
    sys.stdout.write(f"Subtração: {a - b}\n")

def mul(a, b):
    sys.stdout.write(f"Multiplicação: {a * b}\n")

def div_inteiro_resto(a, b):
    if b == 0:
        sys.stdout.write("Erro: divisão por zero\n")
    else:
        sys.stdout.write(f"Divisão inteira: {a // b}\n")
        sys.stdout.write(f"Resto: {a % b}\n")

a = int(sys.argv[1])
b = int(sys.argv[2])

soma(a, b)
sub(a, b)
mul(a, b)
div_inteiro_resto(a, b)"""
















