arreglo = [
    [
        ["amarillo", "rojo", "Naranja"],
        ["Verde", "Blanco", "amarillo"],
        ["rojo", "Naranja", "Verde"]
    ],
    [
        ["Blanco", "amarillo", "rojo"],
        ["Naranja", "Verde", "Blanco"],
        ["amarillo", "rojo", "Naranja"]
    ],
    [
        ["Verde", "Blanco", "amarillo"],
        ["rojo", "Naranja", "Verde"],
        ["Blanco", "amarillo", "rojo"]
    ]
]

contador_amarillo = 0
contador_rojo = 0
contador_Naranja = 0
contador_Verde = 0
contador_Blanco = 0

for capa in arreglo:
    for fila in capa:
        for elemento in fila:
            if elemento == "amarillo":
                contador_amarillo += 1
            elif elemento == "rojo":
                contador_rojo += 1
            elif elemento == "Naranja":
                contador_Naranja += 1
            elif elemento == "Verde":
                contador_Verde += 1
            elif elemento == "Blanco":
                contador_Blanco += 1

print(f"Número de elementos amarillo: {contador_amarillo}")
print(f"Número de elementos rojo: {contador_rojo}")
print(f"Número de elementos Naranja: {contador_Naranja}")
print(f"Número de elementos Verde: {contador_Verde}")
print(f"Número de elementos Blanco: {contador_Blanco}")
