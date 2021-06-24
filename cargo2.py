class cargo:
    def __init__(self):
        self.__codigo=1
        self.descripcion="Docente"

cargo1= cargo()
print(cargo1.__codigo, cargo1.descripcion)
cargo2= cargo()
cargo2.codigo=1
cargo2.descripcion="Docente"
print(cargo2.__codigo, cargo2.descripcion)
cargo3= cargo()
cargo3.codigo=1
cargo3.descripcion="conserje"
print(cargo3.__codigo, cargo3.descripcion)

#################################################################################

class cargo:
    def __init__(self):
        self.__codigo=1
        self.descripcion="Docente"

cargo1= cargo()
print("cargo1", cargo1.descripcion)
cargo2= cargo()
cargo2.codigo=1
cargo2.descripcion="Docente"
print("cargo2", cargo2.descripcion)
cargo3= cargo()
cargo3.codigo=1
cargo3.descripcion="conserje"
print("cargo3", cargo3.descripcion)

##################################################################################

class cargo:
    def __init__(self):
        self.__codigo=99
        self.descripcion="sin cargo"

cargo1= cargo()
print(cargo1.__codigo, cargo1.descripcion)
cargo2= cargo()
cargo2.codigo=1
cargo2.descripcion="Docente"
print(cargo2.__codigo, cargo2.descripcion)
cargo3= cargo()
cargo3.codigo=1
cargo3.descripcion="conserje"
print(cargo3.__codigo, cargo3.descripcion)

#################################################################################

class cargo:
    def __init__(self):
        self.__codigo=1
        self.descripcion="sin cargo"

cargo1= cargo()
print("cargo1", cargo1.descripcion)
cargo2= cargo()
cargo2.codigo=1
cargo2.descripcion="Docente"
print("cargo2", cargo2.descripcion)
cargo3= cargo()
cargo3.codigo=2
cargo3.descripcion="conserje"
print("cargo3", cargo3.descripcion)

#########################################################################
class cargo:
    def __init__(self,des="sin cargo"):
        self.__codigo=99
        self.descripcion=des

cargo1= cargo()
print("cargo1", cargo1.descripcion)
cargo2= cargo()
print("cargo2", cargo2.descripcion)
cargo3= cargo()
print("cargo3", cargo3.descripcion)
#############################################################
#########################################################################
class cargo:
    Secuencia=0
    def __init__(self,des="sin cargo"):
        cargo.Secuencia=cargo.Secuencia+1
        self.codigo=cargo.Secuencia
        self.descripcion=des

cargo1= cargo()
print("cargo1", cargo1.codigo, cargo1.descripcion)
cargo2= cargo()
print("cargo2", cargo2.codigo, cargo2.descripcion)
cargo3= cargo()
print("cargo3", cargo3.codigo, cargo3.descripcion)
print(cargo.Secuencia)


