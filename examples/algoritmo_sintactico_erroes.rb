# algoritmo_sintactico_errores.rb
# Archivo de prueba para GENERAR errores sintácticos en el parser

# Asignación correcta (para que no todo sea error)
a = 10
b = 5

# ===============================
# ERROR 1: if SIN 'end'
# ===============================
if a > b
  puts "a es mayor que b"
  a = a - 1
# Aquí falta el 'end' del if

# ===============================
# ERROR 2: while SIN 'end'
# ===============================
while a > 0
  a = a - 1
  puts a
# Aquí también falta el 'end' del while

# ===============================
# ERROR 3: array mal cerrado
# ===============================
numeros = [1, 2, 3

# ===============================
# ERROR 4: asignación incompleta
# ===============================
c = 

# ===============================
# ERROR 5: uso raro de 'gets' (mal ubicado)
# ===============================
x = gets
y = 
gets

# Esta última línea debería generar un error serio de sintaxis
