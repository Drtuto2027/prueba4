class Persona:
   def __init__ (self, nombre, edad):
       self.__nombre = nombre
       self.__edad = edad

# Getter para el nombre
   def get_nombre(self):
       return self.__nombre

# Setter para el nombre
   def set_nombre(self, nombre):
       self.__nombre = nombre

# Getter para la edad
   def get_edad(self):
       return self.__edad
   
   # Setter para la edad, controlando que no sea negativa
   def set_edad(self, edad):
       if edad >= 0:
         self. edad = edad
       else:
           print("La edad no puede ser negativa.")

# Uso de la clase Persona
persona = Persona("Ana", 25)

# Intentando acceder a los atributos privados (esto causará error)
# print(persona ._ nombre) # No se puede acceder directamente

# Acceder a través de los métodos públicos
print(persona.get_nombre()) # Ana
print(persona.get_edad()) # 25

# Cambiar el valor usando setters
persona.set_nombre("Juan")
persona.set_edad(30)

# Intentar establecer una edad negativa
persona.set_edad(-5) # No permitirá la edad negativa

# Verificar cambios
print(persona.get_nombre()) # Juan
print(persona.get_edad())   #30

# 30