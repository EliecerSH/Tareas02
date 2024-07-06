nombres=[]
election=0

print("inicio de session")

while election !=5:
    print("""
    =====seleccione una opcion=====
          
          1).Inicio de secion
          2).Registrar usuario
          3).Eliminar usuario
          4).registro de usuario
          5).Salir
          """)
    try:
      election=int(input())
    except ValueError:
        print(" solo se aceptan numeros enteros del 1 al 4 ")
    if election==1:
        nom=input(" Ingrese su usuario ")
        if nom == nombres:
            print(" Iniciacion correcta ")
        else:
            print(" erro en la inizacion ")
    elif election==2:
        while election !=3:
            print("""==== Quiere registrar un usuario ====
                  2).Si
                  3).NO""")
            try:
              election=int(input())
            except ValueError:
                print(" solo se permiten numeros enteros 2 y 3 ")
            if election==2:
                addnombre=input(" Ingrese el usuario ")
                nombres.append(addnombre)
    elif election==3:
        while election==3:
            print("""===Quiere eliminar un usuario===
                  1).SI
                  2).NO""")
            try:
              election=int(input())
            except ValueError:
                print(" solo se aceptan numeros enteros 1 y 3 ")
            if election==1:
                rmnombre=input("ingrese el usuario a eliminar ")
                nombres.remove(rmnombre)
    elif election==4:
        print(nombres)
    elif election==5:
        print(" termino de proceso ")