# lexer/log_lexico.py
import os
from datetime import datetime
from .ruby_lexer import construir_lexer

# Carpeta de logs: .../logs/lex
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(os.path.dirname(BASE_DIR), "logs", "lex")


def analizar_y_log(codigo_fuente: str, usuario_git: str) -> tuple:
    """
    Ejecuta el analizador léxico sobre el código Ruby recibido
    y genera un archivo de log con los tokens y errores léxicos.
    Devuelve una tupla (lista_de_tokens_formateados, ruta_archivo_log)
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    lexer = construir_lexer()
    lexer.input(codigo_fuente)

    tokens = []
    tokens_formateados = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
        tokens_formateados.append(f"Tipo: {tok.type}, Valor: {tok.value}")

    ahora = datetime.now()
    fecha = ahora.strftime("%d%m%Y")
    hora = ahora.strftime("%Hh%M")

    nombre_archivo = f"lexico-{usuario_git}-{fecha}-{hora}.txt"
    ruta_archivo = os.path.join(LOG_DIR, nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        if tokens_formateados:
            for token_str in tokens_formateados:
                f.write(token_str + "\n")
        else:
            f.write("No se encontraron tokens.\n")

    return tokens_formateados, ruta_archivo