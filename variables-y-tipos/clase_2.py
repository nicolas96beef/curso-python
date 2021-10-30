"""
Reglas para nombrar variables

En Python existen una serie de reglas para los nombres de variables:
1. Sólo pueden contener los siguientes caracteres
    • Letras minúsculas.
    • Letras mayúsculas.
    • Dígitos.
    • Guiones bajos (_).
2. Deben empezar con una letra o un guión bajo, nunca con un dígito.
3. No pueden ser una palabra reservada del lenguaje

Podemos obtener un listado de las palabras reservadas del lenguaje de la siguiente forma

help('keywords')

--------------------------------------------------

Importante: Los nombres de variables son «case-sensitive / sensibles a minúsculas y mayúsculas»
Por ejemplo: mi_variable y Mi_variable son nombres diferentes.

--------------------------------------------------

Convenciones para nombres

Mientras se sigan las reglas que hemos visto para nombrar variables no hay problema en la
forma en la que se escriban, pero sí existe una convención para la nomenclatura de las
variables. Se utiliza el llamado snake_case en el que utilizamos caracteres en minúsculas
(incluyendo dígitos si procede) junto con guiones bajos – cuando sean necesarios para su
legibilidad –. Por ejemplo, para nombrar una variable que almacene el número de canciones
en nuestro ordenador, podríamos usar num_songs.
Esta convención, y muchas otras, están definidas en un documento denominado PEP 8. Se
trata de una guía de estilo para escribir código en Python. Los PEPs5
son las propuestas que se hacen para la mejora del lenguaje.


---------------------------------------------------
Constantes

Un caso especial y que vale la pena destacar son las constantes. Podríamos decir que es un
tipo de variable pero que su valor no cambia a lo largo de nuestro programa. Por ejemplo
la velocidad de la luz. Sabemos que su valor es constante de 300.000 km/s. En el caso
de las constantes utilizamos mayúsculas (incluyendo guiones bajos si es necesario) para
nombrarlas. Para la velocidad de la luz nuestra constante se podría llamar: ""LIGHT_SPEED"".
PI = 3.14
print(PI)

--------------------------------------------------

Lenguajes Tipados vs Lenguajes Dinamicos

tipados -> asignan el tipo de la variable durante la definicion
dinamicos -> asignan el tipo de la variable durante la ejecucion

python es un lenguaje dinamico

Definicion de una variable
    mi_variable = 1

Como sabemos de la variable?
type(nombre_de_la_variable)

"""