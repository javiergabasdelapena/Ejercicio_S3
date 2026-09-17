def multiplicar(a, b):
    resultado = 0
    while b > 0:
        resultado += a
        b -= 1
    return resultado

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    
    cociente = 0
    while a >= b:
        a -= b
        cociente += 1
    return cociente
print(dividir(10, 2))