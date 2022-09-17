"""
Crie um algoritmo que receba um numero a ser adivinhado por um jogador.
Se ele acertar, parabenize-o, se não, diga que errou
"""
import random

numero = random.randrange(1,10)
resp = "s"
tentativas = 1

while resp=="s":
    chute = int(input("Escreva um numero (de 0 a 10): "))
    if numero==chute:
        print(f"Parabens, voce acertou o numero em {tentativas} tentativas.")
        resp="t"
    else:
        print("Errado.")
        tentativas = int(tentativas) + 1
        resp = str(input("Deseja continuar?(s/n) "))
    if resp=="n":
        print(f"O numero era: {numero}")
        print(f"Voce fez {tentativas} tentativas.")
