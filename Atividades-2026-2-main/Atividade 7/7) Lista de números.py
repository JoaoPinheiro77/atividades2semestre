n = int(input("Quantidade de números: "))

lista = []
for i in range(n):
    valor = float(input("Número: "))
    lista.append(valor)

print("Maior:", max(lista))
print("Menor:", min(lista))
print("Média:", sum(lista)/len(lista))