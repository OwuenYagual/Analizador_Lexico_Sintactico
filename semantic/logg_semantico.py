# Generador de logs

import datetime
import os

errores = []

def agregar_error(mensaje):
    """
    Agrega un error a la lista global de errores.
    """
    errores.append(mensaje)


def guardar_log(usuario_git):
    # Crear carpetas si no existen
    ruta_logs = os.path.join("logs", "sem")
    os.makedirs(ruta_logs, exist_ok=True)

    # Nombre del archivo
    ahora = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    nombre_archivo = f"semantico-{usuario_git}-{ahora}.txt"
    ruta_archivo = os.path.join(ruta_logs, nombre_archivo)

    # Guardar log
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        if len(errores) == 0:
            f.write("✔️ No se encontraron errores semánticos.\n")
        else:
            f.write("ERRORES SEMÁNTICOS DETECTADOS:\n")
            f.write("\n".join(errores))

    print(f"[LOG] Archivo generado: {ruta_archivo}")

    errores.clear()
