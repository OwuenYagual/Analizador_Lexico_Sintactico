# parser/log_sintactico.py
import os
from datetime import datetime
from lexer.ruby_lexer import construir_lexer
from .ruby_parser import construir_parser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR  = os.path.join(os.path.dirname(BASE_DIR), "logs", "sint")

def analizar_sintactico_y_log(codigo_fuente: str, usuario_git: str) -> str:
    os.makedirs(LOG_DIR, exist_ok=True)

    lexer = construir_lexer()
    parser, parser_errors = construir_parser()

    # Ejecutar parser
    parser.parse(codigo_fuente, lexer=lexer)

    ahora = datetime.now()
    fecha = ahora.strftime("%d%m%Y")   # OJO: 20062024
    hora  = ahora.strftime("%Hh%M")    # 23h32

    nombre_archivo = f"sintactico-{usuario_git}-{fecha}-{hora}.txt"
    ruta_archivo   = os.path.join(LOG_DIR, nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("ANÁLISIS SINTÁCTICO (Ruby)\n")
        f.write(f"Usuario Git : {usuario_git}\n")
        f.write(f"Fecha       : {ahora}\n")
        f.write("-" * 60 + "\n")
        f.write("ERRORES SINTÁCTICOS:\n\n")

        if parser_errors:
            for err in parser_errors:
                f.write(err + "\n")
        else:
            f.write("Sin errores sintácticos.\n")

    return ruta_archivo
