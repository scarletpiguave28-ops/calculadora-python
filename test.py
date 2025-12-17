from calculadora import sumar

def test_sumar():
    resultado = sumar(2, 3)
    esperado = 5
    if resultado == esperado:
        print("✅ Prueba PASADA")
        exit(0)
    else:
        print(f"❌ Prueba FALLIDA: esperaba {esperado}, obtuvo {resultado}")
        exit(1)

test_sumar()