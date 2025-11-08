import sys

# classe Modelo para criar objetos
class Arquivo:
    nome = "none"
    extensao = "none"
    tamanho = 0

# objeto: Instância da classe
a1 = Arquivo()
a1.nome = "Instrucao"
a1.extensao = "txt"
a1.tamanho = 3900

a2 = Arquivo()
a2.nome = "CNPJ_20250923"
a2.extensao = "pdf"
a2.tamanho = 61600

a3 = Arquivo()
a3.nome = "pagina"
a3.extensao = "html"
a3.tamanho = 363

a4 = Arquivo()
a4.nome = "PDFRascunho"
a4.extensao = "pdf"
a4.tamanho = 5400

# método
def describe(obj):
    sys.stdout.write(
        f"{obj.nome}.{obj.extensao}\t{obj.tamanho} bytes\n"
    )

def describek(obj):
    kb = obj.tamanho / 1024
    sys.stdout.write(
        f"{obj.nome}.{obj.extensao}\t{kb:.1f} KB\n"
    )

describe(a1)
describe(a2)
describe(a3)
describe(a4)

describek(a1)
describek(a2)
describek(a3)
describek(a4)

#com print e usando o construtor personalizado
class Arquivo:
    def __init__(self, nome, extensao, tamanho ):
        self.nome = nome
        self.extensao = extensao
        self.tamanho = tamanho     
      

    def describe(self):
        print(f"{self.nome}.{self.extensao}\t{self.tamanho} bytes")

    def describek(self):
        kb = self.tamanho / 1024
        print(f"{self.nome}.{self.extensao}\t{kb:.1f} KB")

arq1 = Arquivo("CNPJ_20250923", "pdf", 61600)
arq2 = Arquivo("Instrução", "txt", 3900)
arq3 = Arquivo("pagina", "html", 363)
arq4 = Arquivo("PDFRascunho", "pdf", 5400)

lista = [arq1, arq2, arq3, arq4]

print("=== descriçção ===")
for a in lista:
    a.describe()

print("\n=== descrição em kb ===")
for a in lista:
    a.describek()



