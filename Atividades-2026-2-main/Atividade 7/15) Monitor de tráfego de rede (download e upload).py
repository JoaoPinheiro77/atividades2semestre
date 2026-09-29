import psutil
import time

print("MONITOR DE TRÁFEGO DE REDE")
print("Pressione Ctrl+C para parar.")
print("-" * 50)

while True:
    # Primeira leitura
    dados_antes = psutil.net_io_counters()

    # Espera 1 segundo
    time.sleep(1)

    # Segunda leitura
    dados_depois = psutil.net_io_counters()

    # Calcula a diferença
    download = dados_depois.bytes_recv - dados_antes.bytes_recv
    upload = dados_depois.bytes_sent - dados_antes.bytes_sent

    # Converte de bytes para KB
    download_kb = download / 1024
    upload_kb = upload / 1024

    print(f"Download: {download_kb:.2f} kB/s | Upload: {upload_kb:.2f} kB/s")