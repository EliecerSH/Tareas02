Nombres = []
election=0
while election !=2:
    print(f"""
          ===Quiere Agregar Un Nombre===
          
          1).SI
          2).no
          """)
    try:
      election=int(input())
    except ValueError:
       print(" solo se permiten los numeros 1 y 2 ")
    if election==1:
      AddNombre=input(" ingrese el nombre ")
      Nombres.append(AddNombre)
    elif election==2:
        print(" termino de proceso ")