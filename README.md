Anotações importantes: 

no codigo: f"{obj.nome}.{obj.extensao}\t{kb:.1f} KB\t{obj.dataCriacao}\n" -> exercicio 1 material 3 

Símbolo	       Significado
f""	            f-string — permite embutir variáveis
{ }	            onde a variável aparece dentro da string
\t	            tabulação (TAB)
\n	             quebra de linha
:.1f	           formata número float com 1 casa decimal

Suponha:

obj.nome = "foto"
obj.extensao = "jpg"
kb = 2200 / 1024  → 2.148...
obj.dataCriacao = "10/05/2025"


Então:
foto.jpg   2.1 KB   10/05/2025
foto.jpg ← concatenação com .

\t → tabulação

{kb:.1f} → exibe o valor KB com 1 decimal

\t → mais tabulação

\n → quebra de linha no final


o init tem dois underlines __init__

class person:
    ........
    def describe......... (def dentro da classe é um metodo )
def describe ............(na mesma linha é uma funnção)

class Carros:

    quant = 0 -> Atributo de claasse
    

    def __init__(self, marca, modelo, ano=2025, estado="Novo"): --> Um metodo 
        self.marca = marca   -- 
        self.modelo = modelo   ---
        self.ano = ano             ---   4 atibutos do objeto 
        self.estado = estado    ----
        Carros.quant += 1 ->> atibuto de classe 


########### BUSCA BINARIA ######################
busca de valores em arranjos ordenados consistindo em dividir os espaços de busca continualmente 
pela metade ate uma unidade visivel. Funciona apenas com arrays ordenados (Crescente ou decrescente) e
 acesso aleatorio  aos elementos.
Nao funciona em lstas encadeaas (acesso a informação que so acessa a proxima informação) e arrays desordenados 

ao dividir os espaços de busca continualmente ele sempre vai tirando da esquerda por exemplo 19 / 2 = 9,5 ele pega a esquerda pendendo para um numero inteiro (9)

Arranjo:

[1, 3, 5, 7, 9, 11, 12, 13, 14, 16, 23, 24, 26, 27, 29, 32, 33, 36, 38, 39, 40]


Tamanho = 21

🔵 Tentativa 1

Meio = posição 10
Valor = 23

11 < 23 → vai para a esquerda.

🔵 Novo intervalo: índices 0 a 9

Elementos: [1,3,5,7,9,11,12,13,14,16]

🔵 Tentativa 2

Meio = posição:
⌊(0+9)/2⌋=4

Valor = 9

11 > 9 → vai para a direita.

🔵 Novo intervalo: índices 5 a 9

Elementos: [11,12,13,14,16]

Agora sim, intervalo ímpar: 5 elementos.

🔵 Tentativa 3

Meio = posição:

⌊(5+9)/2⌋=7

Valor = 13

11 < 13 → vai para a esquerda

🔵 Novo intervalo: índices 5 a 6

Elementos: [11, 12]

Intervalo par, mas a busca binária escolhe APENAS UM meio:
⌊(5+6)/2⌋=5
🔵 Tentativa 4

Meio = posição 5
Valor = 11 (achou!)

📌 TOTAL DE TENTATIVAS: 4


✅ 1. BUSCA LINEAR

Como funciona:
Você percorre o vetor do início ao fim, elemento por elemento, até encontrar o valor desejado.

Requisitos:

Não precisa estar ordenado.

Funciona para qualquer ordem ou lista bagunçada.

Complexidade:

O(n) → lenta para listas grandes.

✅ 2. BUSCA BINÁRIA

Como funciona:
Você sempre procura no meio do vetor.
Compara o meio com o valor procurado e elimina metade da lista a cada passo.

Requisito principal:

O vetor deve estar OBRIGATORIAMENTE ordenado.

🔼 Binária em ordem CRESCENTE

Se o vetor está ordenado do menor para o maior, a lógica é:

Se o valor procurado é maior que o meio → busca na direita.

Se o valor procurado é menor que o meio → busca na esquerda.

Exemplo:
[1, 4, 7, 9, 12, 14]

Buscar 9:
Pegamos metade → comparamos → movemos direita/esquerda.

🔽 Binária em ordem DECRESCENTE

Se o vetor está ordenado do maior para o menor, a lógica inverte:

Se o valor procurado é maior que o meio → busca na ESQUERDA.

Se o valor procurado é menor → busca na DIREITA.

Exemplo:
[20, 17, 13, 10, 8, 3]

Buscar 10:
Comparações seguem o mesmo método, mas direções são invertidas.