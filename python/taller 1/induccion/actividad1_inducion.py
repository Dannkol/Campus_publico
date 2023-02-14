# -*- coding: utf-8 -*-
"""Actividad1-inducion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1alAloHGHVZYBQK031ufGJjRjDfWWwgz_

1. Qué operadores utiliza Python en los siguientes casos:

<ul style="list-style-type: none;">
  <li>División Modular</li>
  <li>Exponenciación</li>
  <li>División que retorne entero.</li>
      
</ul>
"""

num1 = 2;
num2 = 3;

print(f"El modulo es con el operador %, modulo de {num1} entre {num2} es {num1 % num2}")
print(f"El exponente es con el operador **, exponente de {num1} a la {num2} es {num1 ** num2}")
print(f"La divicion entera es con el operador //, la dicion entera de {num1} entre {num2} es {num1 // num2}")

"""2. En la jerarquía de operadores, cuáles son los que más
prioridad tienen cuando el intérprete de Python los evalúa?

La prioridad de las operaciones va de mayor a menor 

------------------------------------------------------------------------------------
| Operador                                                  |     Reprecentacion   |
|-----------------------------------------------------------|----------------------|
|Operaciones entre paréntesis                               |     ()               |
|Potencia                                                   |        **            |
|Multiplicación y División, módulo o residuo,División entera|  *, /, %, //         |
|Suma y resta                                               |       + -            |
|Operadores relacionales                                    | <, <=, >, >=, !=, == |
|Operador lógico AND                                        |         AND          |
|Operador lógico OR                                         |         OR           |
------------------------------------------------------------------------------------

3. Si hay operadores de igual precedencia, en qué orden se ejecutan? De izquierda a derecha

4. Que son las expresiones regulares en Python?

Las expresiones regulares son patrones que se utilizan para hacer coincidir combinaciones de caracteres en cadenas.

5. Enumere 5 tipos de datos en Python y suministre un valor de ejemplo de cada uno.
"""

datoint = 1
datopuntoflotante = 1.3
datonumerocomplx = 1+2j
datobool = False
datostring1 = "Hola mundo"


print(f"tenemos dato int {type(datoint)} = {datoint}")
print(f"tenemos dato floar {type(datopuntoflotante)} = {datopuntoflotante}")
print(f"tenemos dato complejo {type(datonumerocomplx)} en este dato tenemos su parte real {datonumerocomplx.real} y su parte imaginaria {datonumerocomplx.imag} = {datonumerocomplx}")
print(f'tenemos datos bool {type(datobool)} = {datobool}')
print(f'tenemos datos string {type(datostring1)} = {datostring1}')

""" 6. En sus propias palabras, qué son las funciones preconstruidas y proporcione 2 ejemplos.

 Una función es una fórmula predefinida que realiza cálculos utilizando valores específicos en un orden particular. Una de las principales ventajas es que ahorran tiempo porque ya no es necesario que la escribas tú mismo.

 Y las funciones numéricas más usadas:

    * print() dibujar en pantalla

    * sum() Suma la lista de números pasados como argumento.

    * min() Determina el valor mínimo de una lista de números pasados como argumento.

    * max() Determina el valor máximo de una lista de números pasados como argumento.

    * range() Crea una lista aritmética de números según el valor pasado como argumento.

    * str() Convierte un valor numérico en texto.
"""

num1 = [1,2,3]

print('Hola mundo desde print()')
print(f"sum(num1) {num1} = {sum(num1)}")

"""7. Cuál es la diferencia entre un condicional simple y un
condicional compuesto?

  * El condicional simple define la ejecución de una o varias instrucciones si se evalúa una condición como verdadera o falsa.

  * El condicional doble, permite decidir que camino de instrucciones o secuencias diferentes tomar, si el condicional es verdadero se ejecutaran un grupo de instrucciones o una instrucción diferente a que si se evalúa como falso el condicional.

8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados.
"""

edad = 18
conduce = False

if edad >= 18:
  if conduce == True:
    print('aprobado la persona es mayor de edad y condice');
  else:
    print('es mayor de edad pero no puede conducir');
else:
  print('no cumple');

""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad.
"""

valores = {'Nombre': '', 'Tel': '', 'Año de ingreso': '', 'Apellido': '', 'Edad' : ''}

for i in valores:
  dato = input(f'Ingrese el valor para {i}: ')
  valores[i] = dato

print(f"Nombre del empleado es {valores['Nombre']} su telefono es {valores['Tel']} su año de ingreso es {valores['Año de ingreso']} su Apellido es {valores['Apellido']} su edad es {valores['Edad']}")

""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
  - Mes de consumo 
  - Valor kw
  -Total kw consumido en el mes 
  - estrato
"""

mes = 'Enero'
valorkw = 400
totalkwcons = 600
estrato = 2

if estrato < 3 :
  valorkw = (valorkw - (valorkw * 0.05))
  print(f'su estrato es {estrato} por ende tiene un descueto de 5% en el valor wk, ahora su kw cuesta {valorkw}');

print(f'su total a pagar en el mes de {mes} es {valorkw * totalkwcons }')