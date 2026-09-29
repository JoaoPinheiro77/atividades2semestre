import psutil
import time

while True:
    memoria = psutil.virtual_memory()

    total = memoria.total / (1024 ** 2)
    usada = memoria.used / (1024 ** 2)
    livre = memoria.available / (1024 ** 2)
    percentual_livre = memoria.available_percent

    print("\033[H\033[J")

    print("=" * 40)
    print("       MONITOR DE MEMÓRIA RAM")
    print("=" * 40)

    print(f"Memória total:  {total:.2f} MB")
    print(f"Memória usada:  {usada:.2f} MB")
    print(f"Memória livre:  {livre:.2f} MB")
    print(f"Percentual livre: {percentual_livre:.2f}%")

    print("=" * 40)
    print("Atualizando a cada 2 segundos...")

    time.sleep(2)