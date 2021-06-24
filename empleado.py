class empleado:
    secuencia=0
    def __init__(self,cod,nom,sue) :
        empleado.secuencia=empleado.secuencia+1
        self.codigo=empleado.secuencia
        self.nombre=nom
        self.sueldo=sue

    def generarcodigo(self):
          empleado.secuencia=empleado.secuencia+1
          return

############################################################################

class empleado:
    secuencia=0
    def __init__(self,cod,nom,sue) :
        self.codigo=self.generarcodigo()
        self.nombre=nom
        self.sueldo=sue

    def generarcodigo(self):
          empleado.secuencia=empleado.secuencia+1
          return empleado.secuencia

##########################################################################
form cargo1 import cargo2

class empleado:
    secuencia=0
    def __init__(self,cod,nom,sue) :
        self.codigo=self.generarcodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargoempleado=car

    def generarcodigo(self):
          empleado.secuencia=empleado.secuencia+1
          return empleado.secuencia

    def mostar(self):
        print ( "codigo; {} Nombre: {} Cargo ({}): {}" . formato ( self . codigo , self . nombre , self . cargoEmp . codigo , self . cargoEmp . descripcion ))

cargo1 = Cargo ( "Docente" )
emp1 = Empleado ( "Ronald" , 1000 , cargo1 )
emp1 . mostrar ()
emp2 = Empleado ( "Brandon" , 1000 , cargo1 )
emp2 . mostrar ()