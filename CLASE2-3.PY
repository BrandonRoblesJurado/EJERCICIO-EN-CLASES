listanotas = [2, 4, 6, 8, 10]
prom = (listanotas)
print('promedio: {} = {}'.format(listanotas, prom))
x = int(input("Ingrese un numero entero: "))
if x < 0:
    x = 0
    print("negativo cambiado a cero")
elif x == 0:
    print("cero")
elif x == 1:
    print("uno")
else:
    print("Ninguna opcion")
print("ok") if type(x) == int else print("-")

###########################################################################

# funciones de fecha
from datetime import datetime, timedelta, date

hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days=30)
dif, aa, mm, dd = futuro, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd + 2)
print(hoy)
print(fdia)
print(futuro)
print(dif)
print(fecha)

############################################################################

# for in cadena - in(tupla) – in[lista]
cvoc = 0
frase = input("Ingrese frase a usar: ")
for car in frase:
    if car in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        if car in ["A", "E", "I", "O", "U"]:
            continue
        else:
            cvoc = cvoc + 1
print("""Cantidad vocales:{}""".format(cvoc))


def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)


oracion = input('Ingrese una oracion: ')
vocales(oracion.lower())


################################################################################################

####taller en clases, Replica realizada por el estudiante####

# num=20
# nombre="ana"
# print(num,type(num))
# print(nombre,type(nombre))
# def mensaje(msg):
#     print(msg)

# mensaje("mi primer programa")
# mensaje("mi segundo programa")

class sintaxis:
    instancia = 0

    # __init__ metodoconstructor que se ejecuta cuando se intancia la clase cuyo onjetivo es
    # crear e instanciar los atributos de la clase. self es un objeto que representa la clase creada.

    def __init__(self, dato="llamando al constructor1"):
        self.frase = dato  # -------> #atributos de instancia
        sintaxis.instancia = sintaxis.instancia + 1

    def usovariables(self):
        edad, peso = 20, 70, 5
        nombres = 'Brandon Robles Jurado'
        tipo_de_sexo = "M"
        civil: True
        # print("civil={}y su tipo es:{}",format(civil,type(civil)))
        usuario = ()
        usuario = ("Broblesj", "2001", "Broblesj@gmail.com", True)
        #             0      1      2             3
        x = usuario[0]
        materia = ["programacion web", "php", "poo"]
        materia.append("go")

        estudiante = {}
        estudiante = {"nombre": "Brandon", "edad": 20, "fac": "faci", }
        estudiante["edad"] = 20
        # print(materia,materia[2:],materia[:2],mateia[:-1],materia[-2:])
        print("x,y")
        print(estudiante, estudiante["nombre"])

    def mostrar(self):
        print("mostrar")
        print(self.frase)


ejer1 = sintaxis()
ejer1.usovariables()

######################################################################

# Tuplas – Listas - Diccionarios
usuario = ('Broblesj', '2001', 'Broblesj@gmail.com')
materias = ['Python', 'PHP', 'POO', 'Go']
alumno = {'nombre': 'Brandon', 'edad': 20, 'fac': 'faci'}
print(usuario[0], materias[1], alumno['nombre'])
print(usuario[0:2], alumno.keys(), alumno.values())
materias.append('Programacion Movil')
alumno['sexo'], alumno['edad'] = 'M', 20
print(materias, alumno)
tupla, lista, diccionario = (), [], {}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i, ':', c)
# Recorridos diccionario con items
for c, v in alumno.items(): print(c, ':', v)

#########################################################################################

[car for car in ['a', 'e', 'i', 'o', 'u'] if car not in ('a', 'i', 'o')]
edad, _peso = 20, 70.5
nombres = 'Brandon Robles Jurado'
dirDomiciliaria = "Av. mariscal sucre antigua y naranzal"
Tipo_sexo = 'M'
civil = True
usuario = ('Broblesj', '2001', 'Broblesj@gmail.com')
materias = ['Programacion Web', 'PHP', 'POO']
docente = {'nombre': 'Josue', 'edad': 20}
print("""Mi nombre es {}, tengo {}      años""".format(nombres, edad))
print(usuario, materias, docente)
import math

num1, num2, num, men = 12.572, 15.4, 4, '1234'
print(math.ceil(num1), '\t', math.floor(num1))
print(round(num1, 1), '\t', type(num), '\t', type(men))

##########################################################################################################################################

# ejemplo de funciones en cadenas
mensaje = 'Bienvenidos' + ' a mi nuevo ' + 'Programa de python'
men1 = mensaje.split()
men2 = ' '.join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("a mi nuevo"), mensaje.lower())


###############################################################################################

class For:
    def __init__(self):
        pass

    def usoFor(self):
        # ciclo repetitivo de incremento o decremento se ejecuta por verdadero
        true = 0
        nombre = "Brandon"
        datos = ["Brandon", 20, true]
        numeros = (2, 5.6, 4, 1)
        docente = {'nombre': 'Brandon', 'edad': 20, 'fac': 'faci'}
        listanotas = [(30, 40), (20, 40), (50, 40)]
        listaalumnos = [{"nombre": "Ronald", "final": 70}, {"nombre": "Julia", "final": 60},
                        {"nombre": "Mirtha", "final": 90}]
        j = 0
        while j < 5:
            print("while", j)
            j = j + 1
        print()
        for i in range(5):
            print("for", i, end=" ")
        print()
        for i in range(1, 5):
            print("for", i, end=" ")
        print()
        for i in range(2, 10, 2):
            print("for", i, end=" ")
        print()
        for i in range(12, 3, -3):
            print("for", i, end=" ")
        print()

        print("_________________________________________")
        lon = len(datos)
        for pos in range(lon):
            print(pos, datos[pos])
        print()
        print("_________________________________________")
        lon = len(numeros)
        for pos in range(lon):
            print(pos, numeros[pos])
        print()
        print("_________________________________________")
        for elem in nombre:
            print(elem, end=" ")
        print()
        print("_________________________________________")
        for pos, valor in enumerate(datos):
            print(pos, valor, end=" ")
        for clave, valor in docente.items():
            print(clave, valor, end=" ")
        print()
        print("_________________________________________")

        for notas in listanotas:
            print("for externo", notas)
            for nota in notas:
                print(nota, end=" ")

            print("saliendo del for interno")
        print("_________________________________________")

        for notas in listanotas:
            acum = 0
            for nota in notas:
                acum = acum + nota
            print(acum / 2, end=" ")

        print()
        print("_________________________________________")
        listaalumnos = [{"nombre": "Ronald", "Final": 70}, {"nombre": "Julia", "Final": 60},
                        {"nombre": "Mirtha", "Final": 90}]
        print("\nDiccionario de alumnos")
        print(listaalumnos)
        acum = 0
        acum = 0
        for alumnos in listaalumnos:
            print(alumnos)
            for clave, valor in alumnos.items():
                print(clave, ":", valor, type(valor), end=" ")
                if type(valor) == int:
                    acum = acum + valor
            print()
        print("Promedio", acum / 3)
        print()
        print("_________________________________________")


bucle = For()
bucle.usoFor()

##########################################################################################

# for range(v) – range(vi,vf)  - range(vi,vf,inc)
frase = input("Ingrese frase a usar: ")
for indice in range(len(frase)):
    print(indice, '=', frase[indice])


###############################################################################################################################

class condicion:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2
        numero = self.numero1 + self.numero2
        self.numero3 = numero

    def condicion(self):
        if self.numero1 == self.numero2:
            print("numero1:{} y numero2:{} son iguales".format(self.numero1, self.numero2))
        elif self.numero1 < self.numero3:
            print("numero1:{} es menor numero3:{}".format(self.numero1, self.numero3))
        else:
            print("no son iguales")
        print("fin del metodo")


condi1 = condicion(8, 18)
print(condi1.numero3)
print(condi1.condicion())


class ciclo:

    def __init__(self, num=10):
        self.numero = num

    def usowhile(self):
        print("dentro de la clase", self.numero)
        LETRA = ""
        while LETRA not in ("a", "e", "i", "o", "u"):
            LETRA = input("ingrese vocal: ").lower()
            # caracter= caracter.lower()

        print("si es la letra correcta:{} si es vocal".format(LETRA))


ciclo1 = ciclo()
print("fuera de la clase", ciclo1.numero)
print(ciclo1.usowhile())


##################################################################################################################################

class For:
    def usoFor(self):

        listasNotas = [(30, 40, 10, 20), (20, 40, 50), (50, 40, 10), (10, 20)]
        acum, cont = 0, 0
        for notas in listasNotas:
            print(notas)
            acump = 0
            contp = 0
            for nota in notas:
                acump += nota
                acum = acum + nota
                cont = cont + 1
            print(acump / len(notas))
        print(acum / cont)


bucle = For()
bucle.usoFor()


##################################################################################################################################

##cargo##

class Cargo:
    def __init__(self):
        self.codigo = 99
        self.descripcion = "sin cargo"


cargo1 = Cargo()
print("cargo1", cargo1.codigo, cargo1.descripcion)

cargo2 = Cargo()
cargo2.codigo = 1
cargo2.descripcion = "docente"
print("cargo2", cargo2.codigo, cargo2.descripcion)

cargo3 = Cargo()
cargo3.descripcion = "conserje"
print("cargo3", cargo3.codigo, cargo3.descripcion)


####################################################################################################################################################

##cargo2##

class Cargo:
    secuencia = 0

    def __init__(self, des="sin cargo"):
        Cargo.secuencia = Cargo.secuencia + 1
        self.codigo = Cargo.secuencia
        self.descripcion = des


if __name__ == "__main__":
    cargo1 = Cargo()
    print("cargo1", cargo1.codigo, cargo1.descripcion)

    cargo2 = Cargo("docente")
    print("cargo2", cargo2.codigo, cargo2.descripcion)

    cargo3 = Cargo()
    print("cargo3", cargo3.codigo, cargo3.descripcion)
    print(Cargo.secuencia)

###########################################################################################################################################################

from cargo2 import Cargo


class Empleado:
    secuencia = 0

    def __init__(self, nom="", sue="", car=None):
        self.codigo = self.generarCodigo()
        self.nombre = nom
        self.sueldo = sue
        self.cargoEmp = car

    def generarCodigo(self):
        Empleado.secuencia = Empleado.secuencia + 1
        return Empleado.secuencia

    def mostrar(self):
        print("codigo;{} Nombre:{} Cargo({}):{}".format(self.codigo, self.nombre, self.cargoEmp.codigo,
                                                        self.cargoEmp.descripcion))


cargo1 = Cargo("Docente")
emp1 = Empleado("Ronald", 1000, cargo1)
emp1.mostrar()
emp2 = Empleado("Brandon", 1000, cargo1)
emp2.mostrar()