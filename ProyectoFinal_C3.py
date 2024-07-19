import pickle

class Empleado():
 def _init_(self):   
    def __init__(self, nom, apell, edad, sal,dni, fechav):              
      self.__nombre = nom
      self.__apellido = apell
      self.__edad = edad
      self.__salario = sal
      self._dni = dni
      self.__fechavin = fechav
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"  
          
    def getSueldo(self):
      return f" Empleado: { self.nombre_completo()}, dni: {self.dni}, sueldo: {self.salario}"
    
    def empleado_informacion(self):
      return (f" Nombre: { self.nombre_completo()}, edad: {self.edad}, sueldo: {self.salario}",
              f"cedula: { self.dni}, fecha de vinculacion: {self.fechav}\n")
    
class Jefe(Empleado):
    def __init__(self, nom, apell, edad, sal, dni, fechav):
        super().__init__(nom, apell, edad, sal, dni, fechav)
        self.empleAcargo = []  
         
    def agregar_empleado(self, empleado):
        for emple in self.empleAcargo:
          if emp == empleado : 
            print(f"Empleado {empleado.nombre_completo()} ya esta a cargo del jefe {self.nombre_completo()}.")
            return     
        self.empleAcargo.append(empleado)
        print(f"Empleado {empleado.nombre_completo()} ya esta agreado al area {self.nombre_completo()}.")
            
    def eliminar_empleados(self, dni):
      for empl in self.empleados:
        if empl == id:
          empl.empleados.remove(empl)
          print (f"Empleado {empleado.nombre_completo()} eliminado del area {self.nombre()}.")
          return
      print (f"Empleado {empleado.nombre_completo()} ya esta a cargo del jefe {self.nombre_completo()}.")
        
   def get_empleados_a_cargo(self):
        return [empleado.nombre_completo() for empleado in self.empleados_a_cargo]
    
    def get_informacion(self):
        empleados_str = ",".join(self.get_empleados_a_cargo()) or "Ninguno"
        return super().get_informacion_emp() + f"\nEmpleados a cargo: {empleados_str}\n"
    
class Area:
    def __init__(self, nombre, descripcion):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.empleados = []
        self.jefe_area = None
    
    def agregar_empleado(self, empleado):
        for emp in self.empleados:
            if emp == empleado:
                print(f"Empleado {empleado.nombre_completo()} ya está en el área {self.__nombre}.\n")
                return
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre_completo()} agregado al área {self.__nombre}.\n")
        
    def eliminar_empleado(self, id):
        for emp in self.empleados:
            if emp == id:
                self.empleados.remove(emp)
                print(f"Empleado {emp.nombre_completo()} eliminado del área {self.__nombre}.\n")
                return
        print(f"No se encontró empleado con cédula {id} en el área {self.__nombre}.\n")
    
    def asignar_jefe(self, jefe):
        if isinstance(jefe, Jefe):
            self.jefe_area = jefe
            print(f"Jefe {jefe.nombre_completo()} asignado al área {self.__nombre}.\n")
    
    def get_jefe_area(self):
        return self.jefe_area.nombre_completo() if self.jefe_area else "Ninguno\n"
    
    def get_empleados(self):
        return [empleado.nombre_completo() for empleado in self.empleados]
    
    def get_informacion(self):
        empleados_str = ", ".join(self.get_empleados()) or "Ninguno\n"
        jefe_str = self.get_jefe_area()
        return f"Área: {self.__nombre}, Descripción: {self.__descripcion}\nJefe Área: {jefe_str}, Empleados: {empleados_str}\n"

    
empleado1 = Empleado("Alex", "Pérez", 30, 5000000, "12345678", "2024-01-15")
empleado2 = Empleado("Maria", "García", 28, 4800000, "87654321", "2024-03-10")

jefe = Jefe("Carlos", "López", 45, 7000000, "11223344", "2024-06-01")
jefe.agregar_empleado(empleado1)
jefe.agregar_empleado(empleado2)
jefe.agregar_empleado(empleado1)

area = Area("ÁREA QA", "Área encargada del testeo de software")
area.agregar_empleado(jefe)
area.agregar_empleado(empleado1)
area.agregar_empleado(empleado2)
area.asignar_jefe(jefe)

print(empleado1.get_informacion_emp())
print(empleado2.get_informacion_emp())
print(jefe.get_informacion())
print(area.get_informacion()) 

print(empleado1.get_sueldo())
print(empleado2.get_sueldo()) 
print(jefe.get_sueldo())

area.eliminar_empleado(empleado1)
jefe.eliminar_empleado(empleado1)


def guardar_datos(empleado, jefe, area):
    with open('datos_empleados.pkl', 'wb') as f:
        pickle.dump((empleado, jefe, area), f)

def cargar_datos():
    try:
        with open('datos_empleados.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return [], [], []

empleados, jefes, areas = cargar_datos()
