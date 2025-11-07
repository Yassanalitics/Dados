import sys 
#classe Modelo para criar objetos
class Arquivo:
 #atributos: Característica (dados)
 nome = "none" #string
 extensao = "none" #string
 tamanho = 0 #float
 dataCriação = 0 #string
#objeto: Instância da classe
a1 = Arquivo ()
a1.nome = "Instrucao"
a1.extensao = "txt"
a1.tamanho = 3900

sys.stdout.write(a1.nome +"."+ a1.extensao +" "+ str(a1.tamanho) +" "+ "bytes.\n")

#metordo/comoprtamento: Ação (função)
def describe(Arquivo):
    sys.stdout.write(f"O arquivo {a1.nome}.{a1.extensao} possui {a1.tamanho} bytes.\n")
describe(Arquivo)

#exemplo em Pyhton sem o sys :
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

p = Pessoa("Ana", 25)
p.apresentar()
#init é o construtor, sempre vai ser utilizado se a sua classe se inicia com atributos especificos 
