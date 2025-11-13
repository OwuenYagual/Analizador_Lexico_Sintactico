# bin/run_lex.py
import sys
import os

# Ruta raíz del proyecto: .../ANALIZADOR_LEXICO_SINTACTICO
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from lexer.log_lexico import analizar_y_log


def main():
    if len(sys.argv) < 3:
        print("Uso: python bin/run_lex.py archivo.rb usuarioGit")
        sys.exit(1)

    ruta_fuente = sys.argv[1]
    usuario_git = sys.argv[2]

    if not os.path.isfile(ruta_fuente):
        print(f"Error: No se encontró el archivo {ruta_fuente}")
        sys.exit(1)

    with open(ruta_fuente, "r", encoding="utf-8") as f:
        codigo = f.read()

    ruta_log = analizar_y_log(codigo, usuario_git)

    print("Análisis léxico completado correctamente.")
    print(f"Log generado en: {ruta_log}")


if __name__ == "__main__":
    main()
