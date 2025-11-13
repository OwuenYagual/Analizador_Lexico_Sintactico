# algoritmo1.rb
# Algoritmo de prueba para el analizador léxico de Ruby

# Comentario de una línea

=begin
  Comentario multilínea para probar =begin ... =end
  Debe ser ignorado por el analizador léxico.
=end

# Constantes especiales
ruta_archivo = _FILE_
linea_actual = _LINE_

number_int   = 42
number_float = 3.1415
cadena_doble = "Hola, Ruby #{number_int}"
cadena_simple = 'Cadena simple sin interpolación'

# Operadores aritméticos
a = 10
b = 3
suma        = a + b
resta       = a - b
producto    = a * b
division    = a / b
modulo      = a % b
potencia    = a ** b

# Operadores relacionales y lógicos
es_mayor      = a > b
es_menor      = a < b
es_mayor_igual = a >= b
es_menor_igual = a <= b
es_igual      = a == b
es_distinto   = a != b

cond1 = true
cond2 = false
logico_y   = cond1 && cond2
logico_o   = cond1 || cond2
logico_not = !cond1

logico_and_palabra = cond1 and cond2
logico_or_palabra  = cond1 or cond2
logico_not_palabra = not cond2

# Arreglos y hashes
numeros = [1, 2, 3, 4, 5]
mi_hash = { "nombre" => "Ana", "edad" => 25, "activo" => true }

# Rango
rango = 1..10
rango_exclusivo = 1...10

# Definición de módulo y clase
module Utilidades
  def self.sumar(x, y)
    x + y
  end
end

class Persona
  def initialize(nombre, edad)
    @nombre = nombre
    @edad   = edad
  end

  def mayor_de_edad?
    @edad >= 18
  end

  def descripcion
    "Persona #{@nombre} con #{@edad} años"
  end

  def saludar
    puts "Hola, soy #{@nombre}"
  end

  # Prueba de return, self y super (aunque no hay herencia real aquí)
  def ejemplo_return
    valor = Utilidades.sumar(1, 2)
    return valor
  end
end

alias PersonaAlias Persona

# Uso de if / elsif / else / unless / until
persona = Persona.new("Carlos", 20)

if persona.mayor_de_edad?
  mensaje = "Es mayor de edad"
elsif persona.mayor_de_edad? == false
  mensaje = "Es menor de edad"
else
  mensaje = "Edad desconocida"
end

unless persona.mayor_de_edad? == false
  estado = "Puede entrar"
end

contador = 0
until contador >= 3
  contador = contador + 1
end

# while con next y break
i = 0
while i < 5
  i = i + 1
  next if i == 2
  break if i == 4
end

# for y CASE
for n in numeros
  case n
  when 1, 2
    # do opcional en case
    resultado = "Número pequeño"
  when 3..4
    resultado = "Número mediano"
  else
    resultado = "Número grande"
  end
end

# begin / rescue / ensure / retry (solo para probar tokens)
intento = 0

begin
  intento = intento + 1
  x = 10 / (intento - 1)   # aquí puede lanzar error en intento == 1
rescue ZeroDivisionError
  # retry solo para que el lexer vea la palabra
  retry if intento < 2
rescue StandardError
  mensaje_error = "Otro error"
ensure
  # ensure siempre se ejecuta
  finalizado = true
end

# Definición y uso de yield, self y super dentro de un contexto artificial
def con_bloque(valor)
  if block_given?
    yield valor
  end
end

con_bloque(5) do |v|
  puts "Valor desde yield: #{v}"
end

# Uso de defined?
var_inexistente = nil
definido = defined?(var_inexistente)

# Undef ficticio para probar token
def metodo_temporal
  123
end

undef metodo_temporal
