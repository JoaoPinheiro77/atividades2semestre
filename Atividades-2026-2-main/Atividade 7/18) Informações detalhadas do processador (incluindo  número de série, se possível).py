import psutil
import platform

print("=" * 50)
print("INFORMAÇÕES DO PROCESSADOR")
print("=" * 50)

# Nome/modelo do processador
processador = platform.processor()

if processador:
    print(f"Modelo: {processador}")
else:
    print("Modelo: Não foi possível identificar")

# Núcleos físicos
nucleos_fisicos = psutil.cpu_count(logical=False)
print(f"Núcleos físicos: {nucleos_fisicos}")

# Núcleos lógicos
nucleos_logicos = psutil.cpu_count(logical=True)
print(f"Núcleos lógicos: {nucleos_logicos}")

# Frequência do processador
frequencia = psutil.cpu_freq()

if frequencia:
    print(f"Frequência atual: {frequencia.current:.2f} MHz")
    print(f"Frequência mínima: {frequencia.min:.2f} MHz")
    print(f"Frequência máxima: {frequencia.max:.2f} MHz")
else:
    print("Frequência: Não foi possível obter")

# Número de série
print("Número de série: Não foi possível obter.")
print("O sistema operacional pode não permitir acesso ao número")
print("de série do processador de forma portátil.")

print("=" * 50)