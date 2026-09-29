import psutil
from datetime import datetime
import time

print("HISTÓRICO DE USO DA CPU")
print("Registrando dados... Pressione Ctrl+C para parar.")

while True:
    # Pega o uso da CPU
    uso_cpu = psutil.cpu_percent(interval=1)

    # Pega a data e hora atual
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Monta a linha do registro
    registro = f"{data_hora} - CPU: {uso_cpu}%\n"

    # Salva no arquivo
    with open("cpu_log.txt", "a") as arquivo:
        arquivo.write(registro)

    print(registro, end="")

    # Espera 5 segundos
    time.sleep(5)