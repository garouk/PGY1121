entradanino=5500
entradajoven=7000
enrtradaadulto=9000
EN=0
EJ=0
EA=0
sw=1
entradastotales=0	

while (sw == 1):
 
 print("Bienvenido al cine Moro")
 print(" ")
 print("Las entradas se distribuyen en 3 secciones: ")
 print("1-Niños (Entre 1-13 años): $5.500")
 print("2-Joven (Entre 14-21 años): $7.000")
 print("3-Adulto (Mayor a 22 años): $9.000")
 print("Para terminar la compra presione 0")
 print(" ")
 
 seleccion = int(input("Seleccione una opcion:"))
 print(" ")
 if seleccion == 1:
  EN = int(input("Cuantas entradas de niño desea llevar: "))
  entradastotales + EN
  print(" ")
 if seleccion == 2:
  EJ = int(input("Cuantas entradas de joven desea llevar: "))
  entradastotales + EJ
  print(" ")
 if seleccion == 3:
  EA = int(input("Cuantas entradas de adulto desea llevar: "))
  entradastotales + EA
  print(" ")
 totalentradas = (EN * entradanino) + (EJ * entradajoven) + (EA * enrtradaadulto)
 if seleccion == 0:
  if EN >= 1:
   print(f"Cantidad de entradas de niño: {EN} Precio: ${EN * entradanino} ")
   print(" ")
  if EJ >= 1:
   print(f"Cantidad de entradas de joven: {EJ} Precio: ${EJ * entradajoven} ")
   print(" ")
  if EA >= 1:
   print(f"Cantidad de entradas de adulto: {EA} Precio: ${EA * enrtradaadulto} ")
   print(" ")
  print(f"Sub total: ${totalentradas}")
  totalventradas = (EN + EJ + EA)
  sw = int(input("Presione 1 para continuar comprando/Presione 2 para salir: "))
  if sw == 2:
   print("Disfrute su funcion")
   print(f"Porcentaje entradas niños: {(EN / totalventradas) * 100}%")
   print(f"Porcentaje entradas joven: {(EJ / totalventradas) * 100}%")
   print(f"Porcentaje entradas adulto: {(EA / totalventradas) * 100}%")