import random

numero = random.randrange(1,10)
resp = "s"
tentativas = 10

print(numero)
while tentativas>=0:
    chute = int(input("Escreva um numero (de 0 a 10): "))
    if numero==chute:
        print(f"Parabens, voce acertou o numero sobrando {tentativas} tentativas.")
        resp="t"
    else:
        print("Errado.")
        tentativas = int(tentativas) - 1
    if tentativas==0:
        print("Suas tentativas acabaram.")
        print(f"O numero era: {numero}")
