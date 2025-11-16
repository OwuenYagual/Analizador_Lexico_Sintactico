def evaluar_numeros(n1, n2, n3)
    limite = gets
    suma = n1 + n2 + n3
    promedio = suma / 3
    mayor = promedio > 10 && n1 < n2
    numeros = [n1, n2, n3, suma, promedio]
    if mayor
        puts promedio
    end
    if n1 > n2 then
        puts n1
    end
    while suma > 0 do
        suma = suma - 2
    end
    n1 += n3
    puts n1
end