import sys

arr = [2, 4, 5, 6, 7, 8, 10, 11]

def main():
    if len(sys.argv) < 2:
        sys.stdout.write("Nenhum parâmetro fornecido.\n")
        return

    comando = sys.argv[1]

# -proc
    if comando == "-proc":
        if len(sys.argv) < 3:
            sys.stdout.write("Informe um valor para -proc.\n")
            return
        try:
            val = int(sys.argv[2])
        except ValueError:
            sys.stdout.write("Valor inválido.\n")
            return
        try:
            pos = arr.index(val)
            sys.stdout.write(f"{val} encontrado na posição {pos}\n")
        except ValueError:
            sys.stdout.write(f"{val} não encontrado\n")

  # -menores
    elif comando == "-menores":
        if len(sys.argv) < 3:
            sys.stdout.write("Informe um valor para -menores.\n")
            return
        try:
            val = int(sys.argv[2])
        except ValueError:
            sys.stdout.write("Valor inválido.\n")
            return
        menores = [x for x in arr if x < val]
        sys.stdout.write(f"Valores menores que {val}: {menores}\n" if menores else "Nenhum valor menor encontrado\n")

# -maiores
    elif comando == "-maiores":
        if len(sys.argv) < 3:
            sys.stdout.write("Informe um valor para -maiores.\n")
            return
        try:
            val = int(sys.argv[2])
        except ValueError:
            sys.stdout.write("Valor inválido.\n")
            return
        maiores = [x for x in arr if x >= val]
        sys.stdout.write(f"Valores maiores ou iguais a {val}: {maiores}\n" if maiores else "Nenhum valor maior encontrado\n")

 # -pares
    elif comando == "-pares":
        pares = [x for x in arr if x % 2 == 0]
        sys.stdout.write(f"Valores pares: {pares}\n" if pares else "Nenhum valor par encontrado\n")

# -pi
    elif comando == "-pi":
        pares = [x for x in arr if x % 2 == 0]
        impares = [x for x in arr if x % 2 != 0]
        sys.stdout.write(f"Pares: {pares}\nÍmpares: {impares}\n")

# -somai
    elif comando == "-somai":
        impares = [x for x in arr if x % 2 != 0]
        soma = sum(impares)
        sys.stdout.write(f"Soma dos ímpares: {soma}\n" if impares else "Nenhum valor ímpar para somar\n")

# -maior
    elif comando == "-maior":
        if arr:
            maior = max(arr)
            sys.stdout.write(f"Maior valor do arranjo: {maior}\n")
        else:
            sys.stdout.write("Arranjo vazio\n")

    else:
        sys.stdout.write("Parâmetro inválido\n")

if __name__ == "__main__":
    main()
