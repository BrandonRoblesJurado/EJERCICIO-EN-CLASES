####VARIABLES DE PYTHON####

#Numericos
edad,_peso=50,70.5

#String
nombres="Daniel Vera"
dirDomiciliaria="Chile y Guayaquil"
Tipo_sexo="M"

#Boolean
civil=True

#Colecciones
usuario=("dchiki","1234","chiki@gmail.com")
materias=("Programacion web","PHP","POO")
docente={"nombre":"Daniel","edad":50,"fac":faci}

#imprimir
print("""Mi nombre es{},tengo{}años""".format(nombres,edad))
print(usuario,materias,docente)

#############################################################

####ESTRUCTURAS DE CONTROL DE PYTHON -IF####

x=int(input("Ingrese un numero entero: "))
if x<0:
    x=0
    print("Negativo cambiadoa cero")
elif x==0:
    print("Cero")
elif x==1:
    print("uno")
else:
    print("Ninguna opcion")
print("Ok") if type(x) == int else print("-")

###############################################################

####ESRUCTURA DE CONTROLDE PYTHON - WHILE####

"uso de while infinito"
c =1
print(c)

# while validacion
vocal = input("ingrese vocal")
while vocal not in ("a","e","i","o","u"):
    if vocal ==".":
        break
    vocal = imput("vocal:")
print("su vocal o punto es: {}".format(vocal))

###############################################################

####ESTRUCTURA DE CONTROL DE PYTHON -FOR####

# FOR RANGE(V)-range (vi,vf)-range(vi,vf,inc)
frase = input("ingrese frase:")
for indice in range(len(frase)):
    print(indice), "=",frase[indise]

# for in cadena - in (tupla) - in [lista]
for car in frase:
    if car in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        if car in ["A", "E", "I", "O", "U"]:
            continue
        else:
          cvoc = cvoc + 1
print("cantidad vocales: {} ".format(cvoc))

# Comprehension – [var for var in datos condicion]
[car for car in ['a', 'e', 'i', 'o', 'u'] if car not in ('a', 'i', 'o')]

#######################################################################################################################################################################

####FUNCIONES EN PYTHON -DEF####

"Funciones sin retorno"
def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)

"Llamada a funcion"
oracion = input("Ingrese oracion: ")
vocales(oracion.lower())

"Funcion con retorno de valor"
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

"llamada a funcion"
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
print("Promedio: {} = {}".format(listanotas, prom))

####################################################################

"Funciones matematicas"
import math
num1, num2, num, men = 12.572, 15.4, 4, '1234'
print(math.ceil(num1), '\t', math.floor(num1))
print(round(num1, 1), '\t', type(num), '\t', type(men))

# funciones de cadenas
mensaje = 'Hola ' + 'mundo ' + "Python"
men1 = mensaje.split()
men2 = ' '.join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("mundo"), mensaje.lower())
