import csv
import json

def es_ganador(run):

    digitos = run[:-2][-2:]
    return digitos in ('92', '95', '84')

with open('listadoRun.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    ganadores = []

    for row in csv_reader:
        run = row['run']
        nombre = row['nombre']
        if es_ganador(run):
            ganadores.append({'run': run, 'nombre': nombre})

with open('ganadores.json', mode='w', encoding='utf-8') as json_file:
    json.dump(ganadores, json_file, ensure_ascii=False, indent=4)

print("RUN ganadores han sido guardados en 'ganadores.json'.")