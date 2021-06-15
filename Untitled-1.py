class Fraccion:
    def __init__ (self,numerador,denominador):
        self.num = numerador
        self.den = denominador
    def show (self):
        print(self.num,"/" , self.den)

x = Fraccion(1,2)
y = Fraccion(2,3)
print(x.show())
print(x.show())


"uso de while infinito"
c =1
print(c)

#while validacion
vocal = input("ingrese vocal")
while vocal not in(´a´,´e´,´i´,´o´,´u´):
    if vocal==´.´:
        break
    vocal = imput("vocal:")
print(´su vocal o punto es :{}´.format(vocal))



#FOR RANGE(V)-range (vi,vf)-range(vi,vf,inc)
frase = input("ingrese frase:")
for indice in range (len(frase)):
    print(indice), ´=´frase [indise]

#for in cadena - in (tupla) - in [lista
for car in frase
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print("cantidad vocales: {} ".format(cvoc) )

# Comprehension – [var for var in datos condicion]
[car for car in['a','e','i','o','u'] if car not in('a','i','o')]
   
#Funciones sin retorno
def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u'):
            print(car

‘’Llamada a funcion’’’
oracion = input('Ingrese oracion: ‘)
vocales(oracion.lower())


#Funcion con retorno de valor
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)


# llamada a funcion
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
print(‘Promedio: {} = {}'.format(listanotas, prom))


#Funciones matematicas
import math
num1, num2, num, men = 12.572,  15.4,  4,  '1234'
print(math.ceil(num1), '\t',math.floor(num1))
print(round(num1,1),'\t',type(num),'\t',type(men))

# funciones de cadenas
mensaje = 'Hola ' + 'mundo ' + 'Python’
men1=mensaje.split()
men2=' '.join(men1)
print(mensaje[0],mensaje[0:4],men1,men2)
print(mensaje.find("mundo"), mensaje.lower())


# funciones de fecha
from datetime import datetime,timedelta,date
hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days=30)
dif, aa, mm, dd = futuro – hoy, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd+2)
print(hoy, fdia, futuro, dif, fecha)


# Tuplas – Listas - Diccionarios
usuario = ('dchiki','1234','chiki@gmail.com')
materias = [‘Python','PHP','POO’,’Go']
docente = {'nombre':'Daniel','edad':50,'fac’:’faci'}
print(usuario[0],materias[1],docente['nombre'])
print(usuario[0:2],docente.keys(),docente.values())
materias.append('Programacion Movil')
docente['sexo’], docente['edad']=‘M’, 51
print(materias,docente)
tupla,lista,diccionario=(),[],{}


# Recorridos tuplas y listas con in
for valor in usuario: print(valor)


# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)

# Recorridos diccionario con items
for c, v in docente.items(): print(c,':',v)

#Numericos
edad, _peso = 50, 70.5

#String
nombres = 'Daniel Vera'
dirDomiciliaria= "Chile y Guayaquil"
tipo_sexo = 'M'

#Boolean
civil = True

#Colecciones
usuario = ('dchiki','1234','chiki@gmail.com')
materias = ['Programacion Web','PHP','POO']
docente = {'nombre':'Daniel','edad':50,'fac’:’faci'}

#imprimir
print("""Mi nombre es {}, tengo {}      años""".format(nombres,edad))
print(usuario,materias,docente)

x=int(input("Ingresa un numero entero: "))
if x < 0:
      x = 0
      print('Negativo cambiado a cero')
elif x == 0:
      print('Cero')
elif x == 1:
      print(‘Uno')
else:
      print(‘Ninguna opcion’)
print(“Ok") if type(x) == int else print(“-")
