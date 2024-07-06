import csv
import json

csv_file = 'datos.csv'
mayores = []

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        nombre = row['Nombre']
        edad = int(row['Edad'])
        comuna = row['Comuna']

        estado_edad = 'Mayor de edad' if edad >= 18 else 'Menor de edad'
        
        # Imprimir la información en la consola
        print(f"Nombre: {nombre}, Edad: {edad}, Estado de edad: {estado_edad}, Comuna: {comuna}")
        
        if edad >= 25:
            mayores.append({
                'Nombre': nombre,
                'Edad': edad,
                'Comuna': comuna
            })

json_file = 'mayores.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(mayores, file, ensure_ascii=False, indent=4)

print(f"Los datos de personas mayores o iguales a 25 años se han guardado en {json_file}")
