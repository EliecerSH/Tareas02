election=None
numero1=None
numero2=None
def operacion(numero1,numero2,simbolo):
    try:
        if simbolo=="suma":
          print(f" El resultado es = {numero1+numero2}")
        elif simbolo=="resta":
          print(f" El resultado es = {numero1-numero2}")
        elif simbolo=="multiplicar":
          print(f" El resultado es = {numero1*numero2}")
        elif simbolo=="dividir":
          print(f" El resultado es = {numero1/numero2}")
        elif simbolo=="elevado":
           print(f" El resultado es = {numero1^numero2}")
        else:
           print(" Error, algun digito puede estar erroneo ")
    except ValueError:
       print(" solo se permiten numeros ")
    except ZeroDivisionError:
       print(" ERROR, al intentar dividir entre cero ")

while numero1==None:
   try:
      numero1=float(input(" Ingrese el primer numero "))
   except ValueError:
      print(" solo se pueden ingresar numeros ")

while election==None:
   print("""-----Elige una operacion-----
         1).SUMA
         2).RESTA
         3).MULTIPLICACION
         4).DIVISION
         5).ELEBAR
         """)
   try:
      election=int(input())
   except ValueError:
      print(" solo se permite numeros enteros del 1 al 5")
   if election==1:
      simbolo="suma"
   elif election==2:
      simbolo="resta"
   elif election==3:
      simbolo="multiplicar"
   elif election==4:
      simbolo="dividir"
   elif election==5:
      simbolo="elevado"
   else:
      print(" no se encontro simbolo ")
print(simbolo)
while numero2==None:
   try:
      numero2=float(input(" Ingrese el segundo numero "))
   except ValueError:
      print(" solo se aceptan numeros ")
operacion(numero1,numero2,simbolo)
    