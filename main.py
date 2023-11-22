def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


# Exemplo de uso:
num = int(input("Digite um número: "))
numero_entrada = num
resultado = fatorial(numero_entrada)
print(f"O fatorial de {numero_entrada} é: {resultado}")
