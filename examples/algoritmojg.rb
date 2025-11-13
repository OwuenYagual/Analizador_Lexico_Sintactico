def factorial(n)
    result = 1
    i = 1 
    while i <= n       # prueba: <=, variables, palabras reservadas
      result = result * i
      i = i + 1
    end
    return result
  end
  
  def es_par?(n)
    if n % 2 == 0      # prueba: %, ==, if
      true
    else
      false
    end
  end
  
  # Pruebas básicas
  puts "Factorial de 5:"
  puts factorial(5)
  puts "¿10 es par?"
  puts es_par?(10)
  
  # Probando arrays, hashes y más delimitadores
  lista = [1, 2, 3, 4]
  
  persona = {
    nombre: "Joaquin",
    edad: 23
  }
  
  # Probando operadores extra
  a = 10
  b = 3
  
  c = a ** b        # prueba de operador: **
  d = a / b         # prueba de divide
  e = a % b         # prueba mod
  f = a >= b        # >=
  g = a != b        # !=
  
  puts c
  puts d
  puts e
  puts f
  puts g