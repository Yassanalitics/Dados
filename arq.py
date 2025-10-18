import sys 

class Arquivo:
 nome = "none"
 extensao = "none"
 tamanho = 0

a1 = Arquivo ()
a1.nome = "Instrucao"
a1.extensao = "txt"
a1.tamanho = 3900

sys.stdout.write(a1.nome +"."+ a1.extensao +" "+ str(a1.tamanho) +" "+ "bytes.\n")

def describe(Arquivo):
    sys.stdout.write(f"O arquivo {a1.nome}.{a1.extensao} possui {a1.tamanho} bytes.\n")
describe(Arquivo)


"""class pagina:
    nome = "none"
    extensao = "none "
    """
    