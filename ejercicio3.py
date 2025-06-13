# Tomar una cadena de texto del usuario
texto = input("Ingresa una cadena de texto: ")

# Convertir a mayúsculas
texto_mayus = texto.upper()

# Contar caracteres
longitud = len(texto)

# Verificar si contiene la palabra "Python"
contiene_python = "Python" in texto

# Mostrar los resultados
print(f"Texto en mayúsculas: {texto_mayus}")
print(f"Número de caracteres: {longitud}")
print(f"Contiene la palabra 'Python': {contiene_python}")