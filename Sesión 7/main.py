# Escribe esta línea de código
print("Bienvenidos al entrenamiento con Python, vamos a disfrutar al máximo de esta sesión")

"""
    Descuento en una compra:
    Si compras más de $1000 obtienes un descuento del 20%
    pide el monto de la compra y muestra el precio final
""" 
# Pedir datos por teclado al usuario int entero float decimales str cadenas de caracteres bool booleanos

compra = float(input("Por favor digita el valor de la compra: "))
    

# Si compras más de $1000, obtienes un descuento del 20%
# Siempre que la salida tenga más de un camino de resolución, debo implementar condicionales

# Operadores combinados
# Operadores de asignación =, operadores aritméticos +-*/, operadores lógicos and y, or o, not,
# Operadores de comparación ==, !=, >, <, >=, <=,

if compra > 1000:
    descuento = compra * 0.2
    #compra = compra - descuento # operador de asignación
    compra -= descuento # operador de asignación compuesto
    print(f"El descuento es de {descuento}, por lo tanto su valor a pagar es de: {compra}")