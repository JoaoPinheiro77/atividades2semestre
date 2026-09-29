import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Adivinhe: "))
    tentativas += 1

    if palpite == numero:
        print("Acertou em", tentativas, "tentativas!")
        break
    elif palpite < numero:
        print("Maior")
    else:
        print("Menor")
