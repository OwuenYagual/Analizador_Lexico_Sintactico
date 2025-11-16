# algoritmo_sintactico_OY.rb
# Prueba sintáctica parcial para el parser en PLY

# ======= 1. ASIGNACIONES + EXPRESIONES ARITMÉTICAS =======

a = 10
b = 5
c = a + b * 2
d = (a - b) / 2

# ======= 2. EXPRESIONES LÓGICAS =======

condicion = (a > b) && (c >= d)

# ======= 3. IMPRESIÓN (PUTS) =======

puts "Resultado de la condición:"
puts condicion

# ======= 4. ESTRUCTURA DE CONTROL IF =======

if condicion
  puts "La condición se cumplió"
end

# ======= 5. ESTRUCTURA DE DATOS – ARRAY =======

numeros = [a, b, c, d]
puts numeros
