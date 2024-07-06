
matriz = []

for i in range(3):
    fila = []
    for j in range(4):
        elemento = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))
        fila.append(elemento)
    matriz.append(fila)

print("\nMatriz ingresada:")
for fila in matriz:
    for elemento in fila:
        print(f"{elemento:4}", end=" ")
    print()