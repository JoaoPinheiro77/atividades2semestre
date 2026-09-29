import psutil
import time

limite = float(input("Digite o limite de uso da RAM (%): "))

while True:
    memoria = psutil.virtual_memory()

    uso = memoria.percent
    total = memoria.total / (1024 ** 2)
    usada = memoria.used / (1024 ** 2)

    print("\033[H\033[J")

    print("=" * 40)
    print("       MONITOR DE MEMÓRIA RAM")
    print("=" * 40)

    print(f"Memória total: {total:.2f} MB")
    print(f"Memória usada: {usada:.2f} MB")
    print(f"Uso da RAM: {uso:.2f}%")
    print(f"Limite definido: {limite:.2f}%")

    if uso > limite:
        print("\n⚠️ ALERTA!")
        print("O uso da memória RAM ultrapassou o limite!")

    else:
        print("\nRAM dentro do limite.")

    print("=" * 40)
    print("Atualizando a cada 2 segundos...")
    
    time.sleep(2)