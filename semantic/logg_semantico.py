# Generador de loggs 

import datetime

errores = []

def agregar_error(mensaje):
    """
    Agrega un error a la lista global de errores.
    """
    errores.append(mensaje)


def guardar_log(usuario_git):
    ahora = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    nombre_archivo = f"semantico-{usuario_git}-{ahora}.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        if len(errores) == 0:
            f.write("✔️ No se encontraron errores semánticos.\n")
        else:
            f.write("ERRORES SEMÁNTICOS DETECTADOS:\n")
            f.write("\n".join(errores))

    print(f"[LOG] Archivo generado: {nombre_archivo}")

    errores.clear()
