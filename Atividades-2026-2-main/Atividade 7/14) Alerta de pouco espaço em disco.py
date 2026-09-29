import psutil

limite = 10

print("ALERTA DE POUCO ESPAÇO EM DISCO")
print("-" * 70)

particoes = psutil.disk_partitions()

for particao in particoes:
    try:
        uso = psutil.disk_usage(particao.mountpoint)

        espaco_livre = 100 - uso.percent

        if espaco_livre < limite:
            print(f"ALERTA: A partição {particao.mountpoint} está com pouco espaço!")
            print(f"Espaço livre: {espaco_livre:.1f}%")
            print(f"Espaço usado: {uso.percent:.1f}%")
            print("-" * 70)

    except PermissionError:
        pass