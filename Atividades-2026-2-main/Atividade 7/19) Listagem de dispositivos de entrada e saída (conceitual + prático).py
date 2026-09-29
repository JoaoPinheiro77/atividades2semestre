import psutil

# ==========================================================
# DISPOSITIVOS DE ENTRADA E SAÍDA (E/S)
# ==========================================================
#
# Exemplos de dispositivos de entrada:
# - Teclado
# - Mouse
# - Microfone
# - Webcam
#
# Exemplos de dispositivos de saída:
# - Monitor
# - Impressora
# - Alto-falantes
#
# Dispositivos que podem funcionar como entrada e saída:
# - HD
# - SSD
# - Pendrive
#
# Neste programa vamos detectar as partições de armazenamento
# usando a biblioteca psutil.
# ==========================================================

print("=" * 60)
print("DISPOSITIVOS DE ARMAZENAMENTO")
print("=" * 60)

particoes = psutil.disk_partitions()

if not particoes:
    print("Nenhuma partição encontrada.")
else:
    # Lista as partições
    for i, particao in enumerate(particoes):
        print(f"{i + 1} - {particao.mountpoint}")

    print("=" * 60)

    # Escolha do usuário
    escolha = int(input("Escolha o número da partição: "))

    if escolha < 1 or escolha > len(particoes):
        print("Opção inválida!")

    else:
        particao = particoes[escolha - 1]

        try:
            # Obtém informações da partição escolhida
            uso = psutil.disk_usage(particao.mountpoint)

            total = uso.total / (1024 ** 3)
            usado = uso.used / (1024 ** 3)
            livre = uso.free / (1024 ** 3)

            print("\n" + "=" * 60)
            print("INFORMAÇÕES DO DISPOSITIVO")
            print("=" * 60)

            print(f"Ponto de montagem: {particao.mountpoint}")
            print(f"Sistema de arquivos: {particao.fstype}")
            print(f"Total: {total:.2f} GB")
            print(f"Espaço usado: {usado:.2f} GB")
            print(f"Espaço livre: {livre:.2f} GB")
            print(f"Uso: {uso.percent:.1f}%")

        except PermissionError:
            print("Não foi possível acessar essa partição.")