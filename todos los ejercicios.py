#1.4 Algoritmos y Diagramas de Flujo
#1.4.1 Introducción a los algoritmos
#En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie de un círculo,
#para un radio cualquiera.
print ("Superficie de un Circulo")
pi = 3.1416
radio = int(input("Ingresa el valor del radio: "))
superficie = (radio ** 2) * pi
print ("la superficie es ",  superficie)
###########################################################################################################
#2.3 Estructuras secuenciales
#En una tienda se ofrece un descuento del 15% sobre el total de la compra,
#y un cliente desea saber cuánto deberá pagar finalmente por su compra.
total= float(input("Ingrese el total de la compra: "))
descuento= total*.15
print("El total a pagar es: $", total-descuento)
print("El descuento aplicado es: $", descuento)  
###########################################################################################################
#Obtener la cantidad de dinero que recibirá un vendedor por concepto de comisiones,
#por tres ventas realizadas en el mes, y el total que recibirá en el mes por sueldo y comisión. 
#Se sabe que el vendedor recibe un sueldo base y un 10% extra por comisiones de todas sus ventas.
def calcular(self):
    tv,v1,v2,v3,tr,c,sb=0,0,0,0,0,0,0
    sb=int(print("ingrese sueldo base : "))
    v1=int(print("valor de venta 1: "))
    v2=int(print("valor de venta 2: "))
    v3=int(print("valor de venta 3 : "))
    tv=v1+v2+v3
    c=tv*0.1
    tr=sb+c
    print("cantidad total a resivir",tr)
###########################################################################################################
#2.4.1 Estructuras selectivas simples
#Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba         
def calcular(self):
    cal=int(print("ingrese calificacion : "))
    if  cal >=7:
     print("aprovado") 
###########################################################################################################
#2.4.2 Estructuras selectivas dobles
#Dado como dato la calificación de un alumno en un examen, 
#escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
print("Verificar si el alumno esta aprobado")
cal=float(input("Ingrese la calificacion: "))
if cal>=7:
    print("Aprobado",cal)
else:
    print("Reprobado",cal)
###########################################################################################################
#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento,
#del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
print("Sueldo a Recibir")
sue=float(input("Ingrese Sueldo: "))
if sue<600:
    aum=sue*0.10
    sue=sue+aum
    print("Obtiene aumento",sue)
else:
    print("No obtiene aumento",sue)
print("El sueldo es: ",sue)
###########################################################################################################
#2.4.3 Estructuras selectivas compuestas
#Determinar la cantidad de dinero que recibirá un trabajador,
#por concepto de las horas extras trabajadas en una empresa, 
#sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras,
#y que éstas se pagan al doble de una hora normal, cuando no exceden de 8;
#si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal,
#y el resto al triple.
class tarea:
    def __int__(self):
        pass
    def calcularjornada(self):
        ht, he, het =0,0,0
        ph, phe, pt, ph8=0,0,0,0
        ht=int(input("ingrese horas trabajaras: "))
        ph=float(input("ingrese valor hora: "))
        if ht>40:
            he=ht-40
            if he>8:
                het=he-8
                ph8=8*ph*2
                phe=het*ph*3
            else:
                phe=0
                ph8=he*ph*2
            
            pt=40*ph+ph8+phe
        else:
            pt= ht*ph
            print("sobretiempo<8:{} sobretiempo>8:{} jornda: {} ".format(ph8,phe, pt))
            print("El pago total de horas trabajadas es ", pt)
tarea= tarea()
tarea.calcularjornada()
###########################################################################################################
#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
numeros = []
for i in range(3):
    numero = float(input("Introduce el número {}: ".format(i + 1)))
    numeros.append(numero)
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
         mayor = numero
print("Mayor:", mayor)
###########################################################################################################
#2.4.4 Estructuras selectivas múltiples
#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, 
#obtenga el resultado de la siguiente función:
NUM = int( input("Tipo de Calculo: ")) 
V = int( input("Ingrese Valor: ")) 
Funcion = {
1 : 100*V,
2 : 100^V,
3 : 100/V
}
resp = Funcion.get(NUM, 0)
print("el resultado es:", resp)
###########################################################################################################
#2.4.5 Expresiones lógicas
#Una escuela aplica dos exámenes a sus aspirantes, 
#por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. 
#El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; 
#en caso contrario es rechazado.
print("Calificaciones Denotadas Como C1 Y C2")
C1=float(input("Ingrese la calificacion de C1: "))
C2=float(input("Ingrese la calificacion de C2: "))
if C1>=80:
    print("Aprobado C1",C1)
else:
    print("Rechanado C1",C1)

if C2>=80:
    print("Aprobado C2",C2)
else:
    print("Rechazado C2",C2)
###########################################################################################################
#2.5.2 La estructura FOR
#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado. 
print("Suma de enteros")
suma=0
i=1
for i in range(i,100,i):
         suma=suma+i*i
         print("La suma total de los numeros entero es: ", suma)
###########################################################################################################
#2.5.3 La estructura WHILE
#Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100
print("Escribir los numeros del 1 al 100")
i=1
while i<=100:
    print(i)
    i=i+1
###########################################################################################################
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
#utilizando un bucle controlado por el usuario.
resp=input("Desea ingresar? (S/N) ").lower()
num=int(input("Ingrese un numero: "))
suma=0
prod=1
while resp == "s":
    suma = suma + num
    prod = prod * num
    print(suma, prod)
    resp=input("Desea continuar? (S/N) ").lower()
print("Total de la suma es: ", suma)
print("Total del producto es: ", prod) 
###########################################################################################################
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
#utilizando un bucle controlado por centinela.
num=int(input("Ingrese un numero: "))
resp=input("Ingrese una letra: ").lower()
suma=0
prod=1
while resp != "a":
    suma = suma + num
    prod = prod * num
    print(suma, prod)
    resp=input("Ingrese una letra ").lower()
print("Total de la suma es: ", suma)
print("Total del producto es: ", prod)
###########################################################################################################
#Determinar si un número entero proporcionado por el usuario es primo. 
#Un número primo es un entero que no tiene más divisores que él mismo y la unidad.
num=int(input("Ingrese un numero entero: "))
primo=True
divisor=2
while divisor < num and primo==True:
    res = num % divisor
    if res == 0:
        primo= False
    divisor=divisor+1
if primo == True:
    print("Numero {} es primo".format(num))
else:
    print("Numero {} no es primo".format(num)) 
###########################################################################################################
#2.5.4 La estructura REPEAT
#Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N,
#y calcular el resultado de la siguiente serie: 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. 
#Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.
serie=0
I = 1
N=int(input("Ingrese un numero: "))
band=True
while I<N:
    if band == True:
        serie=serie+(1/I)
        band==False
    else:
        serie=serie-(1/I)
        band==True
    I=I+1

print(serie)
###########################################################################################################
#2.5.6 Bucles anidados
#Calcular el factorial de N números enteros leídos de teclado.
def factorial(self):
    n= int(input("ingrese la cantidad de numero: "))
    for i in range(n):
        numero=int(input("ingrese numero: "))
        acu=1
        for num in range(numero,1,-1):
            acu=acu*num
        print("numero={}  factorial={}".format(numero,acu))
###########################################################################################################
#3.2Arreglos en una dimensión
#Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros,
#y a continuación escribir en un vector A todos los números negativos,
#y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.


###########################################################################################################
#3 Arreglos en dos dimensiones
# Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. 
#Los datos sobre estos exámenes se proporcionan de la siguiente manera:

