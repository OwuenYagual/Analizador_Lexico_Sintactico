# lexer/log_lexico.py
import os
from datetime import datetime
from .ruby_lexer import construir_lexer

# Carpeta de logs: .../logs/lex
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(os.path.dirname(BASE_DIR), "logs", "lex")


def analizar_y_log(codigo_fuente: str, usuario_git: str) -> str:
    """
    Ejecuta el analizador léxico sobre el código Ruby recibido
    y genera un archivo de log con los tokens y errores léxicos.
    Devuelve la ruta completa del archivo de log generado.
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    lexer = construir_lexer()
    lexer.input(codigo_fuente)

    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    ahora = datetime.now()
    fecha = ahora.strftime("%d-%m-%Y")
    hora = ahora.strftime("%Hh%M")

    nombre_archivo = f"lexico-{usuario_git}-{fecha}-{hora}.txt"
    ruta_archivo = os.path.join(LOG_DIR, nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("ANÁLISIS LÉXICO (Ruby)\n")
        f.write(f"Usuario Git : {usuario_git}\n")
        f.write(f"Fecha : {ahora}\n")
        f.write("-" * 60 + "\n")
        f.write("TOKENS:\n")

        for tok in tokens:
            linea = f"L{tok.lineno:3d}"
            f.write(f"{linea} {tok.type:12s} {repr(tok.value)}\n")

        f.write("\n" + "-" * 60 + "\n")
        f.write("ERRORES LÉXICOS:\n")

        if lexer.errors:
            for linea, caracter, mensaje in lexer.errors:
                f.write(f"L{linea:3d} {repr(caracter):6s} {mensaje}\n")
        else:
            f.write("Sin errores léxicos.\n")

        f.write("\nRESUMEN:\n")
        f.write(f"Total de tokens : {len(tokens)}\n")
        f.write(f"Errores léxicos : {len(lexer.errors)}\n")

    return ruta_archivo