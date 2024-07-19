class Empleado():
 def _init_(self):   
    def __init__(self, nom, apell, edad, sal,dni, fechav):              
      self.__nombre = nom
      self.__apellido = apell
      self.__edad = edad
      self._dni = dni
      self.__fechavin = fechav
    
    def obtener_Nombre_Completo(self):
        return f"{self.nombre} {self.apellido}"  
      
      
    def getNombre(self):
      return self.__nombre
    
    def getEdad(self):
      return self.__edad
    
    def getFecha(self):
      return self.__fechav
    
    def setEdad(self, edad):
      self.__edad = edad

empleado1 = Empleado('Andres', 'Prada', 30, 2000000, 1033, 20-03-2023)
#print (f"Nombre del empleado: ", empleado1.getNombre())
#print (f"Edad del empleado: ", empleado1.getEdad())
print(empleado1)

empleado2 = Empleado('Andres', 'Prada', 30, 2000000, 1033, 20-03-2023)
print(empleado2)
empleado3 = Empleado('Andres', 'Prada', 30, 2000000, 1033, 20-03-2023)
print(empleado3)
empleado4 = Empleado('Andres', 'Prada', 30, 2000000, 1033, 20-03-2023)
print(empleado4)

          
    
class Jefe(Empleado):
    def __init__(self, nom, apell, edad, sal, dni, fechav):
        super().__init__(nom, apell, edad, sal, dni, fechav)
        self.empleAcargo = []  
         
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)     
        
    def obtener_cantidad_empleados(self):
      return len(self.empleados)
    
    def obtener_empleados(self):
      return self.empleados
            
class Area():
    def __init__(self, nom, descripcion ):
       self.nombre = nom
       self.descripcion = descripcion
       self.empleados = []
       
  
    def __str__(self):
      return f" Area: {self.nombre}, Descripcion: {self.descripcion}, Cantidad de empleados: {len(self.empleados)}"
        








