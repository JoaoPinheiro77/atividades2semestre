valor = float(input("Valor da prestação: "))
taxa = float(input("Taxa (%): "))
dias = int(input("Dias de atraso: "))

nova = valor + (valor * taxa * dias / 100)
print("Nova prestação:", nova)