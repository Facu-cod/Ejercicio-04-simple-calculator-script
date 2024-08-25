operacion = int(input("""Hola ingresa el numero de la operación que quieras realizar:
    1-Suma
    2-Resta
    3-División
    4-multiplicación
    :"""))

valor1 = float(input("Ingresa el primer valor: "))
valor2 = float(input("Ingresa el segundo valor: "))

if operacion == 1:
    print(f"El resultado de la suma de {valor1} + {valor2 } es = {valor1 + valor2}")
elif operacion == 2:
    print(f"El resultado de la resta de {valor1} - {valor2 } es = {valor1 - valor2}")
elif operacion == 3:
    if valor2 != 0:
        print(f"El resultado de la división de {valor1} / {valor2} es = {valor1 / valor2}")
    else:
        print("Error: No se puede dividir entre 0.")
elif operacion == 4:
    print(f"El resultado de la multiplicación de {valor1} * {valor2 } es = {valor1 * valor2}")
else:
    print("El valor seleccionado no corresponde a una operación valida.")