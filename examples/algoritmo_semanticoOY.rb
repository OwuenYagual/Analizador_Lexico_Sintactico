# algoritmo_semantico.rb
# Pruebas para el analizador semántico

# ----- Casos correctos básicos -----
x = 10
x = 20           # misma variable, mismo tipo (int) → OK

nombre = "Juan"
saludo = "Hola " + nombre   # string + string → OK

n1 = "123".to_i  # conversión válida: string numérico → to_i

# ----- Errores de identificadores -----
if = 5           # 'if' es palabra reservada → identificador inválido
3abc = 10        # identificador no válido (empieza con dígito)

# ----- Errores de tipos en asignación -----
y = 100
y = "hola"       # int → string → incompatibilidad de tipos

# ----- Errores en operaciones -----
z = 5 + "texto"  # int + string → operación inválida

w = "hola" - "mundo"  # string - string → operación inválida

# ----- Errores en conversiones -----
n2 = "abc".to_i  # string no numérico → to_i inválido

b = true
c = b.to_f       # bool → to_f inválido
