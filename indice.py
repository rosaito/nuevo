print ("------------------------------")
print ("1.Agregar")
print ("2.Eliminar")
print ("3.Modificar")
print ("4.Listar")
print ("5.Salir")
print ("------------------------------")

seleccion = None
while seleccion != 5:
    seleccion = input("Ingrese un valor: ")
    if seleccion == "1":
        print("Agregar")
        
    elif seleccion == "2":
        print("Eliminar")
    elif seleccion == "3":
        print ("Modificar")
    elif seleccion == "4":
        print ("Listar")
    elif seleccion=="5":
        print("salir")
        break
exit()
