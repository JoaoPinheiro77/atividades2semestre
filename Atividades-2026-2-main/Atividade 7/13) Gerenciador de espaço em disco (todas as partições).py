import psutil

print("GERENCIADOR DE ESPAÇO EM DISCO")
print("-" * 80)

print(f"{'Partição':<15} {'Total':<15} {'Usado':<15} {'Livre':<15} {'Uso':<10}")
print("-" * 80)

particoes = psutil.disk_partitions()

for particao in particoes:
    try:
        uso = psutil.disk_usage(particao.mountpoint)

        total = uso.total / (1024 ** 3)
        usado = uso.used / (1024 ** 3)
        livre = uso.free / (1024 ** 3)
        porcentagem = uso.percent

        print(
            f"{particao.mountpoint:<15} "
            f"{total:.2f} GB{'':<8} "
            f"{usado:.2f} GB{'':<8} "
            f"{livre:.2f} GB{'':<8} "
            f"{porcentagem:.1f}%"
        )

    except PermissionError:
        pass