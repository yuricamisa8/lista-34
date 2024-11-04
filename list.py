#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
numeros = []
for n in range (5):
    numero = float(input(f"digite o {n + 1 } nunero inteiro"))
    numeros.append(numero)
    for n, numero in enumerate (numeros):
      print(f"numero da posição{n}: {numero}")
