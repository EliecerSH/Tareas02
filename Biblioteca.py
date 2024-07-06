import json
libros=[]
on=1
election=0
def addlibro(titulo,autor):
    libro ={
        "Titulo":titulo,
        "Autor":autor,
        "Estado":"Disponible"}
    libros.append(libro)
    print("-----Linbro agregado-----")

def libroEstado(titulo,estado):
    for libro in libros:
       if libro["Titulo"]==titulo:
          libro["Estado"]=estado
          print("-----Estado de libro cambiado-----")
       else:
           print(" ese libro no esta registrado ")

while on == 1:
    print("""----seleccion un apcion-----
          
          1).Agregar un libro
          2).cambiar estado de libro
          3).ver libros
          4).Cargar libros
          5).Guardar registro
          6).terminar proceso
          """)
    try:
        election=int(input())
    except ValueError:
        print(" solo se aceptan numeros enteros del 1 al 6 ")
    if election==1:
        titulo=input(" Ingrese el titulo del libro = ")
        autor=input(" Ingrese el autor del libro = ")
        addlibro(titulo,autor)
    elif election==2:
        titulo=input(" Ingrese el titulo del libro ")
        estado=input(" Ingrese el estado a cambiar ")
        libroEstado(titulo,estado)
    elif election==3:
        print("-----Libros en la biblioteca-----")
        for libro in libros:
            print(libro)
    elif election==4:
        with open('libros.json','r') as file:
            libros=json.load(file)
            print("-----Registro cargado-----")
    elif election==5:
        with open('libros.json','w') as file:
            json.dump(libros,file,indent=4)
            print("-----Registro guardado-----")
    elif election==6:
        print("-----Termino de proceso-----")
    else:
        print(" no se a detectado comando ")