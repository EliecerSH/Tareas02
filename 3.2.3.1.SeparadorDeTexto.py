texto = input("Ingrese un texto: ")
palabras = texto.split()
frecuencia_palabras = {}
for palabra in palabras:
    palabra = palabra.lower()  
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")
