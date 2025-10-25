import sys 

class Arquivo:
 nome = "none" #string
 extensao = "none" #string
 tamanho = 0 #float
 dataCriação = 0 #string

a1 = Arquivo ()
a1.nome = "Instrucao"
a1.extensao = "txt"
a1.tamanho = 3900

sys.stdout.write(a1.nome +"."+ a1.extensao +" "+ str(a1.tamanho) +" "+ "bytes.\n")

def describe(Arquivo):
    sys.stdout.write(f"O arquivo {a1.nome}.{a1.extensao} possui {a1.tamanho} bytes.\n")
describe(Arquivo)


