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
