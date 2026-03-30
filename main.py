

from funciones import *
cargar_json()
while True:
    print(" \n === MENU GYM ===")
    print("1.Registrar Nuevo cliente")
    print("2.Buscar cliente")
    print("3.Actualizar Datos cliente")
    print("4.Eliminar  cliente")
    print("5.Guardar datos del cliente")
    print("* Salir del Sistema")
    print("="*20)
    optiones_menu = (input("Ingrese un el numero de la actividad a realizar:"))
  
       
    if optiones_menu == "1":
        añadir_cliente()
    elif optiones_menu == "2":
        buscar_cliente()
    elif optiones_menu == "3":
        actualizar_cliente()
    elif optiones_menu == "4":
        eliminar_cliente()
    elif optiones_menu == "5":
        guardar_json()
    elif optiones_menu == "*":
        print("Gracias por usar el sistema hasta pronto ")
        break
        



    
