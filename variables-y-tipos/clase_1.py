"""

Las variables se les asigna un valor con el operador de asignacion '='

Formula para definir y asignar variables


nombre_de_la_variable + operador de asignacion + valor

TIPOS

Números
Python soporta dos tipos de números - enteros (integer) y números de punto flotante o decimales (float). 
Para definir un entero, usa la siguiente sintaxis:

mi_Entero = 7
mi_decimal = 7.6

Cadenas o Strings
Las cadenas están definidas con comillas sencillas o compuestas/dobles.


Ejercicio:

mi_cadena = 'Hola'
mi_cadena_dos = "Mundo"
Guarda en variables los siguientes datos sobre ti: 
Nombre -> mi_nombre
Edad -> mi_edad
Altura en mts -> mi_altura
Juego de pc favorito -> mi_juego_favorito


Resumen:
- variables
- tipos de datos: Enteros, Decimales, Strings
"""
# Escribe tu propio código aquí
mi_nombre = "nicolas besteiro"
mi_edad = 24
mi_altura = 1.84
mi_juego_favorito = "gta"


# probando el código
print(f"Nombre: {mi_nombre}")
print(f"Apuntador: {id(mi_nombre)}")
if isinstance(mi_edad, int):
    print(f"Edad: {mi_edad}")
if isinstance(mi_altura, float):
    print(f"Altura: {mi_altura}")
print(f"Juego de pc favorito: {mi_juego_favorito}")