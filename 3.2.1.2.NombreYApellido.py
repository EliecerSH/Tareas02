nombres = []
apellidos = []
con=1

while con < 4:
    AddNombre = input(f" ingrese nombre {con} ")
    nombres.append(AddNombre)
    addApellido = input(f" ingrese el apellido {con} ")
    apellidos.append(addApellido)
    con = con+1

print("---Nombres---")
for element in nombres:
    print(element)

print("---Apellidos---")
for element in apellidos:
    print(element)