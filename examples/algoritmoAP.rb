def fibonacci(n)
  a = 0
  b = 1
  i = 0

  while i < n
    puts a
    temp = a + b
    a = b
    b = temp
    i = i + 1
  end
end

puts "Ingrese el número de términos:"
num = gets.to_i

if num > 0
  fibonacci(num)
else
  puts "Debe ingresar un número mayor que 0"
end
