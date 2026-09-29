def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("1-Somar 2-Subtrair 3-Multiplicar 4-Dividir")
op = int(input("Escolha: "))

a = float(input("A: "))
b = float(input("B: "))

if op == 1:
    print(somar(a,b))
elif op == 2:
    print(subtrair(a,b))
elif op == 3:
    print(multiplicar(a,b))
elif op == 4:
    print(dividir(a,b))