cesta=[]
productos=["arroz","fideos","lentejas","azucar","sal"]
election=0

while election !=4:
    print("""=== seleccione una opcion ===
          1).Agregar un producto a la cesta
          2).Ver canasta
          3).Ver total
          4).Salir
          """)
    try:
        election=int(input())
    except ValueError:
        print(" solo se permiten numeros enteros del 1 al 4 ")
    if election==1:
        while election !=6:
            print("""===Que producto desea agregar===
            1).Arroz
            2).Fideos
            3).Lentejas
            4).Azucar
            5).Sal
            6).Salir
            """)
            try:
                election=int(input())
            except ValueError:
                print(" solo se permiten numeros enteros del 1 al 6 ")
            if election==1:
                cesta.append(productos[0])
                print(" producto agregado ")
            elif election==2:
                cesta.append(productos[1])
                print(" Producto agregado ")
            elif election==3:
                cesta.append(productos[2])
                print(" Producto agregado ")
            elif election==4:
                cesta.append(productos[3])
                print(" Producto agregado ")
            elif election==5:
                cesta.append(productos[4])
                print(" Producto agregado ")
    elif election==2:
        print(f"""----------Cesta------------
              1).arroz   = {cesta.count("arroz")}
              2).Fideos  = {cesta.count("fideos")}
              3).Lentejas= {cesta.count("lentejas")}
              4).Azucar  = {cesta.count("azucar")}
              5).sal     = {cesta.count("sal")}
              """)
    elif election==3:
        cdarroz=cesta.count("arroz")
        arroz=cdarroz*1500
        cdfideos=cesta.count("fideos")
        fideos=cdfideos*1700
        cdlentejas=cesta.count("lentejas")
        lentejas=cdlentejas*1200
        cdazucar=cesta.count("azucar")
        azucar=cdazucar*1000
        cdsal=cesta.count("sal")
        sal=cdsal*700
        total=arroz+fideos+lentejas+azucar+sal
        print(" el total es $",total)
    elif election==4:
        print("Termino de proceso")