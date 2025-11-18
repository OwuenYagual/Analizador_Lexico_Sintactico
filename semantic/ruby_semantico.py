# ================================
# ruby_semantico.py
# Analizador Semántico para Ruby
# ================================

import re
import sys
from logg_semantico import agregar_error, guardar_log



class RubySemanticAnalyzer:
    def __init__(self):
        self.variables = {}        # nombre → tipo (ej: "x": "int", "nombre": "string")
        self.errores = []          # lista de errores semánticos
        self.linea_actual = 0

        # Lista básica de palabras reservadas de Ruby
        self.palabras_reservadas = {
            "if", "else", "elsif", "end", "while", "do", "class", "def",
            "true", "false", "nil", "puts", "gets", "return"
        }

    # --------------------------------------------------------------
    # Reglas Semánticas
    # --------------------------------------------------------------
    # Integrante1: Owuen Yagual
    #   - Regla 1: Validación de identificadores
    #   - Regla 2: Consistencia de tipos en asignación
    # --------------------------------------------------------------

    def validar_identificador(self, nombre):
        """
        Regla semántica 1:
        Verifica que el identificador sea válido:
        - No puede ser palabra reservada.
        - Debe empezar por letra o guión bajo.
        """
        # ¿Es palabra reservada?
        if nombre in self.palabras_reservadas:
            self.reportar_error(
                f"Línea {self.linea_actual}: identificador inválido '{nombre}', "
                f"es una palabra reservada."
            )
            return False

        # ¿Cumple patrón de identificador? (letra o _ seguido de letras/dígitos/_)
        if not re.match(r'^[A-Za-z_]\w*$', nombre):
            self.reportar_error(
                f"Línea {self.linea_actual}: identificador inválido '{nombre}'."
            )
            return False

        return True

    def registrar_variable(self, nombre, tipo_inicial):
        """
        Regla semántica 2: registro inicial de variable con tipo.
        Si el identificador no es válido, no se registra.
        Si ya existe, no se sobreescribe (se respeta el primer tipo).
        """
        if not self.validar_identificador(nombre):
            # Si el identificador es inválido, no registramos nada
            return

        if nombre not in self.variables:
            self.variables[nombre] = tipo_inicial
        # Si ya existe, NO cambiamos el tipo aquí. La verificación se hace en asignacion_tipo.

    def inferir_tipo_literal(self, valor):
        """
        Intenta inferir el tipo a partir de un literal simple:
        - solo dígitos -> int
        - número con punto -> float (lo tratamos como int/number si quieres simplificar)
        - "algo" o 'algo' -> string
        - true/false -> bool
        - nil -> nil
        - si no se puede inferir, devuelve 'desconocido'
        """
        v = valor.strip()

        # String entre comillas simples o dobles
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            return "string"

        # Booleanos
        if v == "true" or v == "false":
            return "bool"

        # nil
        if v == "nil":
            return "nil"

        # Entero
        if re.fullmatch(r'\d+', v):
            return "int"

        # Flotante (opcionalmente puedes mapearlo también a "int" o "number")
        if re.fullmatch(r'\d+\.\d+', v):
            return "float"

        # Si llega aquí, puede ser una expresión más compleja o variable
        return "desconocido"

    def asignacion_tipo(self, nombre, expresion):
        """
        Regla semántica 2 (OwuenYagual):
        Verifica consistencia de tipos al asignar:
        - Si la variable no existe, se respeta el tipo inferido en registrar_variable().
        - Si ya existe y el nuevo tipo inferido es diferente, se reporta error.
        """
        tipo_inferido = self.inferir_tipo_literal(expresion)

        # Si no podemos inferir tipo (expresión compleja), no rompemos,
        # solo no validamos tipos en esta asignación.
        if tipo_inferido == "desconocido":
            return

        # Si la variable no está registrada por algún motivo, la registramos aquí.
        if nombre not in self.variables:
            self.registrar_variable(nombre, tipo_inferido)
            return

        tipo_actual = self.variables[nombre]

        # Si el tipo cambia (ej.: primero int, luego string), error semántico.
        if tipo_actual != tipo_inferido:
            self.reportar_error(
                f"Línea {self.linea_actual}: asignación incompatible para '{nombre}': "
                f"tipo declarado '{tipo_actual}' y se intenta asignar '{tipo_inferido}'."
            )
        # Si es consistente, no hay nada que hacer.

    # --------------------------------------------------------------
    # Integrante2
    # --------------------------------------------------------------



    # --------------------------------------------------------------
    # Integrante3: Joaquin Guerra
    #   - Regla 3: Operaciones permitidas
    #   - Regla 4: Conversión válida de tipos
    # --------------------------------------------------------------
    def verificar_operaciones(self, expresion):
        """
        Regla Semántica 3:
        Verifica que las operaciones se realicen entre variables o literales compatibles.
        """
        match = re.match(r"(.+)\s*([\+\-\*\/])\s*(.+)", expresion)
        if not match:
            return

        op1, operador, op2 = match.groups()
        op1, op2 = op1.strip(), op2.strip()

        tipo1 = self.inferir_tipo_literal(op1) if op1 not in self.variables else self.variables[op1]
        tipo2 = self.inferir_tipo_literal(op2) if op2 not in self.variables else self.variables[op2]

        if tipo1 == "desconocido" or tipo2 == "desconocido":
            return

        tipos_numericos = {"int", "float"}

        if operador in {"+", "-", "*", "/"}:

            # string + string permitido
            if operador == "+" and tipo1 == "string" and tipo2 == "string":
                return

            # numérico permitido
            if tipo1 in tipos_numericos and tipo2 in tipos_numericos:
                return

            # caso incompatible
            self.reportar_error(
                f"Línea {self.linea_actual}: operación inválida entre '{tipo1}' y '{tipo2}' usando '{operador}'."
            )

    def verificar_conversion(self, expresion):
        """
        Regla Semántica 4:
        Verifica que las conversiones como to_i, to_f, to_s sean válidas
        según el tipo del valor.
        """
        match = re.match(r"(\w+|\'.*?\'|\".*?\")\.(to_i|to_f|to_s)", expresion)
        if not match:
            return

        valor, metodo = match.groups()

        tipo_valor = self.inferir_tipo_literal(valor) if valor not in self.variables else self.variables[valor]

        # to_i y to_f → requieren valores numéricos o strings numéricos
        if metodo in {"to_i", "to_f"}:
            if tipo_valor not in {"int", "float", "string"}:
                self.reportar_error(
                    f"Línea {self.linea_actual}: conversión inválida '{metodo}' para tipo '{tipo_valor}'."
                )
                return

            # string debe ser numérico
            if tipo_valor == "string" and not re.fullmatch(r"['\"]\d+(\.\d+)?['\"]", valor):
                self.reportar_error(
                    f"Línea {self.linea_actual}: no se puede convertir '{valor}' mediante {metodo}, contenido no numérico."
                )

    # --------------------------------------------------------------
    # Utilidades comunes
    # --------------------------------------------------------------

    def reportar_error(self, mensaje):
        self.errores.append(mensaje)

    # --------------------------------------------------------------

    def analizar(self, codigo_rb):
        with open(codigo_rb, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        for i, linea in enumerate(lineas, start=1):
            self.linea_actual = i

            # Ignorar líneas vacías y comentarios simples
            if linea.strip().startswith("#") or linea.strip() == "":
                continue

            # Ej: x = 10
            match_asign = re.match(r"(\w+)\s*=\s*(.+)", linea)
            if match_asign:
                var, val = match_asign.groups()
                var = var.strip()
                val = val.strip()

                if var not in self.variables:
                    # Asumimos tipo inicial básico según el valor
                    tipo = "int" if val.isdigit() else self.inferir_tipo_literal(val)
                    if tipo == "desconocido":
                        # Si no podemos inferir, por defecto string
                        tipo = "string"
                    self.registrar_variable(var, tipo)

                self.asignacion_tipo(var, val)
                # reglas -> operaciones-conversion
                self.verificar_operaciones(val)
                self.verificar_conversion(val)
                continue

            # Ej: x += 1
            match_inc = re.match(r"(\w+)\s*(\+=|-=)\s*(.+)", linea)
            if match_inc:
                var, op, val = match_inc.groups()
                # (verificar_incrementos)
                # self.verificar_incrementos(var)
                continue

            # Aquí se pueden agregar mas patrones

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

    # Agregar errores al logger
    for err in errores:
        agregar_error(err)

    guardar_log(usuario_git)
    print("Análisis semántico terminado.")