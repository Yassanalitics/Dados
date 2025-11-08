class Something:
    name = "none"
    size = 0.0
    
s1 = Something()
s1.name = "Document"
s1.size = 0.8
print(f"The file {s1.name} has a size of {s1.size} MB")

class Person:
    name = "none" 
    altura = 0.0 #metros
    peso = 0 #kg
    idade = 0
    
p1 = Person()
p1.name = "Wesley" #string
p1.altura = 1.75 #float
p1.peso = 70 #int
p1.idade = 28 #int

print(f"Este eh {p1.name} e ele tem {p1.altura} metros de altura, pesa {p1.peso} kg e tem {p1.idade} anos de idade")
def MostrarPessoa (person):
    print(person.name
          +" tem ("
          +str(person.idade)
          +") anos,  "
          +str(person.altura)
          +"m de altura, e "
          +str(person.peso)
          +"kg."
        )
MostrarPessoa(p1)
