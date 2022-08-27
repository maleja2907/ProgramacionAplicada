## 12-TALLER 01
'''
El presente taller tiene como objetivo evaluar las habilidades adquiridas hasta el momento a lo largo del curso,
así como repasar los conceptos e introducir nuevas herramientas.
'''
# Recordatorio, el archivo lo deben subir a su repositorio en la fecha indicada.
## 1. Persistencia (1.0)
l_paises = ['Colombia','Mexico','Turquia','Polonia','serbia','dinamarca','holanda','Alemania']#la lista
l_paises1=""#para añadir los valores a convertir en el txt 
for i in range(0,8,1):#bucle iniciado para recorrer la lista
    l_paises1+=l_paises[i].capitalize()#se indica que cada posicion de la lista va a tener la primer aletra en mayuscula y se agrega al nuevo conjunto 
    l_paises1+=", "#se separa pcada valors por coma y espacio en la variable nueva 
archi1=open("datos.txt","w")#comando utilizado para convertir en un archivo txt
with open('datos.txt', 'w') as temp_file:#comando para abrir el documento txt
    for item in l_paises1:#se inicia un bucle para recorrer el conjunto nuevo n
        temp_file.write("%s" % item)
file = open('datos.txt', 'r')#comando para abrir 
print(file.read())#imprime

#TODO: escriba un programa que le permina escribir de manera automatica los nombres de estos paises en un archivo txt
#NOTA: todos los nombres deben tener una mayuscula al comienzo
#       el archivo se ecuentra en formato csv
## 2. Lectura de archivos (1.0)
str_archivo = open("datos.txt")#llamamiento del archivo 
print(str_archivo.read())#poner el archivo en modo lectura
#TODO: escriba un programa que le permita leer e imprimir el archivo generado anteriormente

## 3. números binario (1.5)
def f_calBin (s_num):
    s_residuo=0
    list=[]
    str_num=str(s_num)
    print(str_num.split(sep="."))
    s1_num=int(str_num[0])
    print(str_num[2])
    s2_num=int(str_num[2])

    while s1_num!=0:
        s_residuo =s1_num % 2
        s1_num=s1_num//2
        list.append(s_residuo)
    k= len(list) - 1
    s_bin=[]
    while (k>= 0):
        s_bin.append(list[k])
        k = k - 1
    s2_num=s2_num*10^(len(str_num[2]))
    for i in range(5):
        s2_num=s2_num*2
        k=str(s2_num)
        print(k[1])
        s_bin.append(int(k[0]))
        s2_num=int(k[2])
    return s_bin
print(f_calBin(4.1))
    '''
    Calculadora que permite encontrar la representación en binario de un número entero o decimal que ingresa por parametro
    :param s_num: número que se desea convertir a binario int o float
    :return: valor número en binario
    '''

    #TODO: escribir la sección del codigo para las conversiones
    #NOTA: puede hacer uso de tantas funciones como necesite (diseñadas por el estudiante)
    # #deben asignal el valor binario en esta variable
    return s_bin
print(f_calBin(4))


#Test

assert f_calBin (1) == 1
assert f_calBin (4) == 100
assert f_calBin (10) == 1010
assert f_calBin (1.25) == 1.01

## 4. Valores estadisticos (1.5)
import numpy as np # se importa la libreria numpy para organizar la lista
l_valores = [9,2, 9, 4, 5, 1, 8, 7, 8, 8, 9, 10,3]#la lista
def f_stat(l_valores):# inicia la funcion con el parametro de entrada que vendria siendo la lista
    s_mean, s_median,str_ordn,int_contadora,int_divisor,str_ordn = 0, 0, 0, 0,len(l_valores),np.sort(l_valores)#se inician todas las variables, las 4 primeros en 0, el int_divisor que es:
    #la cantidad de numeros de la lista y str_ordn que es la variable para ordenar la lista
    s_mean=sum(l_valores)/int_divisor#se actualiza la variable de la media diciendo que va a ser igual a la suma de los valores de la lista dividido la cantidad de nunmeros
    half=int_divisor//2#half es una varible que nos ayudara a conocer el valor mita de la lista teniendo la cantidad de valores de la lista(int_dividor) y dividiendolo en 2
    if int_divisor%2==0:#se inicia la codicion de que si la cantidad de la lista es par
        s_median=(l_valores[half-1]+l_valores[half])/2##la mediana va a ser el valore mitad de la lista mas el valor siguiente al de la mutad de la lista y esp dividido en 2
        #ya que se estrablece para la mediana que si la cantidad de valores de la lista es par el valor es igual a la suma de los 2 valores medios dividido en 2
    else:#de no ser asi
        s_median=l_valores[half]#la mediana es simplemente el valor medio de la lista ordenada
    def mode(l_valores):#funcion para identificar la moda
      frequency = {}#inicia diccionario vacido de la variable frecuencia que nos almacenara la cantidad de veces que un dato esta en la lista
      for value in l_valores:#inicia el bucle para recorrer la lista
          frequency[value] = frequency.get(value, 0) + 1#se realixa para cada valores de la lista que tantas veces se repite
      most_frequent = max(frequency.values())#se indica el valor q tiene mallor frecuenca
      s_moda = [key for key, value in frequency.items()if value == most_frequent]#la moda sera el numero (value) que tenga mas frecuencia

      return s_moda #la funcion de la moda la retorna
    return (f"la media es:{s_mean}, la mediana es: {s_median} y la moda es: {mode(l_valores)}")#la funcion macro retorna el valor de la media moda y mediana como enuncaido 
print(f_stat(l_valores))#llamamiento de la función

## 5. BONO (0.5)
#TODO: realizar la verificación del punto aterior haciendo uso de la función assert (pytest)

pdta//el taller fue realizado en conjunto entre maria alejandra leyton hincapié y juan david panadero maldonado 
