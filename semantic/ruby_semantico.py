# ================================
# ruby_semantico.py
# Analizador Semántico para Ruby
# ================================

import re
import sys
from logg_semantico import escribir_log


class RubySemanticAnalyzer:
    def __init__(self):
        self.variables = {}        # nombre → tipo
        self.errores = []          # lista de errores semánticos
        self.linea_actual = 0

    # --------------------------------------------------------------
    # Reglas Semánticas
    # --------------------------------------------------------------
    # Integrante1



    # --------------------------------------------------------------
    # Integrante2




    # --------------------------------------------------------------
    # Integrante3


    # --------------------------------------------------------------

    def reportar_error(self, mensaje):
        self.errores.append(mensaje)

    # --------------------------------------------------------------

    def analizar(self, codigo_rb):
        with open(codigo_rb, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        for i, linea in enumerate(lineas, start=1):
            self.linea_actual = i

            # Ej: x = 10
            match_asign = re.match(r"(\w+)\s*=\s*(.+)", linea)
            if match_asign:
                var, val = match_asign.groups()
                if var not in self.variables:
                    # asumimos declaración automática tipo int si es dígito
                    tipo = "int" if val.strip().isdigit() else "string"
                    self.registrar_variable(var, tipo)
                self.asignacion_tipo(var, val.strip())
                continue

            # Ej: x += 1
            match_inc = re.match(r"(\w+)\s*(\+=|-=)\s*(.+)", linea)
            if match_inc:
                var, op, val = match_inc.groups()
                self.verificar_incrementos(var)
                continue

            # Aquí puedes agregar más patrones si lo necesitas

        return self.errores


# ==========================================

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python ruby_semantico.py archivo.rb usuarioGit")
        sys.exit(1)

    archivo_rb = sys.argv[1]
    usuario_git = sys.argv[2]

    analizador = RubySemanticAnalyzer()
    errores = analizador.analizar(archivo_rb)

    escribir_log(usuario_git, errores)
    print("Análisis semántico terminado.")
