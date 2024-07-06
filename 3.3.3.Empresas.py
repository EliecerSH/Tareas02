import csv
import json

empresas = []

with open('listadoRutEmpresa.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ventas = int(row['ventas'])
        if ventas <= 100000000:
            clasificacion = "Pequeño Contribuyente"
        elif ventas <= 200000000:
            clasificacion = "Mediano Contribuyente"
        else:
            clasificacion = "Gran Contribuyente"
        
        row['clasificacionEmpresa'] = clasificacion
        empresas.append(row)

with open('segmentacionEmpresas.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(empresas, jsonfile, ensure_ascii=False, indent=4)

print("Archivo segmentacionEmpresas.json creado correctamente.")
