class Empleado():   
    def __init__(self, nom, apell, edad, salario, dni, fecha_vinculacion):              
      self.__nombre = nom
      self.__apellido = apell
      self.__edad = edad
      self.salario = salario
      self.dni = dni
      self.fecha_vinculacion = fecha_vinculacion
      
listaEmpl=[]

def Mostrar():
    k=0
    while k< len(listaEmpl()):
        print(listaEmpl[k])
        k += 1
i= 0
while(True):
    print(" 1. Registrar empleado")
    print("2. Consultar listado")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    
    if(opcion == 1):
        print("Ir a Registrar")
        nom = input("Nombre: ")
        apel = input("Apellido: ")
        edad = int(input("Edad: "))
        nom = input("Nombre: ")
        empleado1 = Empleado(nom, apel, edad)
        listaEmpl.append(empleado1)
        print("empleado guardado exitosamente")
        
        
    elif(opcion ==2):
        #print("ir a mostrar")
        Mostrar()
    elif(opcion ==3):
        exit()
    else:
        print("opcion no valida. Intentelo de nuevo")
            