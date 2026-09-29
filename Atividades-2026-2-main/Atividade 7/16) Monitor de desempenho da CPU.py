import psutil

print("MONITOR DE DESEMPENHO DA CPU")
print("Pressione Ctrl+C para parar.")
print("-" * 50)

while True:
    # Uso da CPU por núcleo
    nucleos = psutil.cpu_percent(interval=1, percpu=True)

    # Calcula o uso total da CPU
    total = psutil.cpu_percent(interval=None)

    print(f"CPU Total: {total:.1f}%")

    for i, uso in enumerate(nucleos):
        print(f"Núcleo {i}: {uso:.1f}%", end=" | ")

    print("\n" + "-" * 50)