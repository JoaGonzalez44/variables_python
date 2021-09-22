# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

Val_1 = float(input("inserte el primer valor... "))
Val_2 = float(input("inserte el segundo valor... "))
if Val_2 == 0:
  Val_2 = float(input("por favor elija un numero distinto de cero para el segundo valor:  "))
Suma = Val_1 + Val_2
Resta = Val_1 - Val_2
Multiplicación = Val_1 * Val_2 
División = Val_1/Val_2 
Potencia = Val_1 ** Val_2 
print(f"la suma entre {Val_1} y {Val_2} es {Suma}")
print(f"la resta entre {Val_1} y {Val_2} es {Resta}")
print(f"la multiplicacion entre {Val_1} y {Val_2} es {Multiplicación}")
print(f"la division entre {Val_1} y {Val_2} es {División}")
print(f"{Val_1} elevado a {Val_2} es {Potencia}")