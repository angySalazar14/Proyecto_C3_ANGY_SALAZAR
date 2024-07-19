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
    
    def __str__(self):
      return f" Empleado: {self.obtener_nombre_completo}, edad: {self.edad}, Salario: {self.sal},
      DNI: {self.dni}, Fecha de vinculacion:  {self.fechav}"
        
empleado1 = Empleado('Andres', 'Prada', 30, 2000000, 1033, "20-03-2023")
#print (f"Nombre del empleado: ", empleado1.getNombre())
#print (f"Edad del empleado: ", empleado1.getEdad())

print(empleado1)

#empleado1.setEdad(57)
#print(empleado1.getEdad())
#print(empleado1.getFecha())   

class Jefe(Empleado):
    def __init__(self, nom, apell, edad, sal, dni, fechav):
        super().__init__(nom, apell, edad, sal, dni, fechav)
        self.empleAcargo = []  
         
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado) 
             


