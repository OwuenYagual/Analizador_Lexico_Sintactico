import os
import datetime
import subprocess
from ruby_lexer import lexer

CARPETA_LOGS = "../logs"

def obtener_usuario_git():
    try:
        resultado = subprocess.check_output(
            ["git", "config", "user.name"],
            text=True
        ).strip()
        return resultado.replace(" ", "").lower()
    except:
        return "usuario_desconocido"

def analizar_archivo(ruta_archivo, usuario_git=None):
    if usuario_git is None:
        usuario_git = obtener_usuario_git()

    os.makedirs(CARPETA_LOGS, exist_ok=True)

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        data = f.read()

    lexer.input(data)

    ahora = datetime.datetime.now()
    timestamp = ahora.strftime("%d-%m-%Y-%Hh%M")
    nombre_log = f"lexico-{usuario_git}-{timestamp}.txt"
    ruta_log = os.path.join(CARPETA_LOGS, nombre_log)

    with open(ruta_log, "w", encoding="utf-8") as log:
        log.write(f"LOG ANALISIS LEXICO\n")
        log.write(f"Archivo: {ruta_archivo}\n")
        log.write(f"Usuario Git: {usuario_git}\n")
        log.write(f"Fecha: {ahora}\n")
        log.write("-" * 60 + "\n")

        while True:
            tok = lexer.token()
            if not tok:
                break
            log.write(f"Línea {tok.lineno:<4} Tipo {tok.type:<12} Valor {tok.value}\n")

    print(f"Log generado en: {ruta_log}")


if __name__ == "__main__":
    import sys

    archivo = sys.argv[1] if len(sys.argv) >= 2 else None
    usuario = sys.argv[2] if len(sys.argv) >= 3 else None

    if archivo is None:
        print("Uso: python log_lex.py <archivo.rb> [usuarioGit]")
    else:
        analizar_archivo(archivo, usuario)