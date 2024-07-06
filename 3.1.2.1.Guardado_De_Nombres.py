nombres = []
con=1

while con < 4:
    AddNombre=input(" ingrese nombre ")
    nombres.append(AddNombre)
    con = con+1

nombre_Con_Max_Caracteres = max(nombres, key=lambda palabra: len(palabra))
print("El nombre con más caracteres es:", nombre_Con_Max_Caracteres)