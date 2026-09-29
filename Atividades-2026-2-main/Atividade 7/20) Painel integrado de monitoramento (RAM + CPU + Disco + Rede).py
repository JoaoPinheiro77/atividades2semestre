import psutil
import time
import os

print("PAINEL DE MONITORAMENTO")
print("Pressione Ctrl+C para parar.")

while True:

    # ==================================================
    # RAM
    # ==================================================
    memoria = psutil.virtual_memory()

    ram_percentual = memoria.percent
    ram_usada = memoria.used / (1024 ** 2)

    # ==================================================
    # CPU
    # ==================================================
    cpu = psutil.cpu_percent(interval=1)

    # ==================================================
    # DISCO
    # ==================================================
    # Pega a partição principal do sistema
    particao_principal = psutil.disk_partitions()[0]

    disco = psutil.disk_usage(particao_principal.mountpoint)

    disco_livre = disco.free / (1024 ** 3)

    # ==================================================
    # REDE
    # ==================================================
    rede_antes = psutil.net_io_counters()

    time.sleep(1)

    rede_depois = psutil.net_io_counters()

    download = rede_depois.bytes_recv - rede_antes.bytes_recv
    upload = rede_depois.bytes_sent - rede_antes.bytes_sent

    download_kb = download / 1024
    upload_kb = upload / 1024

    # ==================================================
    # LIMPA A TELA
    # ==================================================
    os.system("cls" if os.name == "nt" else "clear")

    # ==================================================
    # EXIBE O PAINEL
    # ==================================================
    print("=" * 55)
    print("              PAINEL DE MONITORAMENTO")
    print("=" * 55)

    print(f"RAM:       {ram_percentual:.1f}% usada")
    print(f"RAM usada: {ram_usada:.2f} MB")

    print("-" * 55)

    print(f"CPU:       {cpu:.1f}%")

    print("-" * 55)

    print(f"Disco:     {particao_principal.mountpoint}")
    print(f"Espaço livre: {disco_livre:.2f} GB")

    print("-" * 55)

    print(f"Download:  {download_kb:.2f} kB/s")
    print(f"Upload:    {upload_kb:.2f} kB/s")

    print("=" * 55)
    print("Atualizando...")

    # Espera 2 segundos antes da próxima atualização
    time.sleep(2)