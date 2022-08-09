## EJERCICIO 01
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones (por ahora no importa qué son), así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
##
def f_suma (a,b):# tenemos la iniciacion de la función con el nombre "f_suma" y que contará con los parametros iniciales "a,b "
    a+=b #se indica con el operador "+" que se desea realizar la adicion de "b" a "a"
    return a # se retorna el valor actualizado de "a"
  
  
  
  
  
# Se genera un error si no funciona de manera adecuada
assert f_suma(3,5) == 8
assert f_suma(3,-5) == -2
assert f_suma(-7,-5) == -12
## modulo

def f_mod(a,b):# tenemos la iniciacion de la función con el nombre "f_mod" y que contará con los parámetros iniciales "a,b "
    c=b%a #se indica con el operador "%" que se desea conocer el residuo de la divicion entre "b" y "a" siendo "a" el divisor y "b" el divisor 

    return c

# Se genera un error si no funciona de manera adecuada
assert f_mod(3,5) == 2
assert f_mod(3,-5) == -1
assert f_mod(4,10) == 2

## Cadenas de caracteres
def f_str_01 (str_01):
    str_02 = print(str_01.split())
    print(str_02.upper())
    return str_02

assert f_str_01('Hola Mundo') == 'HolaMUNDO'
assert f_str_01('tengo un dinosaurio') == 'tengoUNdinosaurio'
