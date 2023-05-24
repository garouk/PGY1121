# Ejemplo de uso de repositorio

print("Datos personales")
print(" ")
s = 1
vNom = input("Ingrese su nombre: ")
print(" ")
while s==1: 

    try:
     vEdad = int(input("Ingrese su edad: "))
     break
    except Exception as vEr:
        print("Ingrese una edad valida")

print(" ")
print(f"Su nombre es: {vNom} \nSu edad es: {vEdad}")
D = int(input("1 Si desea continuar, 2 Si desea salir: "))
if D == 2:
       s = 2

    
print("Programa finalizado")



