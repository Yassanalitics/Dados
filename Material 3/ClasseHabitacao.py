#Exercicio 3 
class CasaModelo:
    codPlanta = "none"
    tamanho = 0
    engenheiro = "none"
    custo = 0.0 
    tempo = 0
    def __init__(self, codPlanta, tamanho, engenheiro, custo, tempo):
        self.codPlanta = codPlanta
        self.tamanho = tamanho #metros quadrados 
        self.engenheiro = engenheiro #responsável
        self.custo = custo 
        self.tempo = tempo #tempo estimado para conclusão 
    def toString(self):
        return (f"Código da Planta: {self.codPlanta}\n Tamanho: {self.tamanho} m2\n  Engenheiro Responsável: {self.engenheiro}\n Custo da construção: {self.custo}\n Tempo estimado para Conclusão: {self.tempo} meses. ")

c1 = CasaModelo("PLT001", 120, "Engenheiro A", 250000.00, 6 )
c2 = CasaModelo("PLT002", 150, "Engenheiro B", 300000.00, 8 )


#função para exibir todas as casas 
Lista = [c1,c2]

print("=== CASAS MODELO ===")
for a in Lista:
    print (a.toString())
    
print (c1.toString())
print (c2.toString())

    