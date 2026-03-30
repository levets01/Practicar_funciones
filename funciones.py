
clientes = []

def añadir_cliente():

    id_cliente = int(input("Ingrese el Id del cliente:"))
    name = input("Ingrese el nombre del cliente:").lower()
    edad = int((input("Ingrese la edad del cliente:")))
    plan = input("Ingrese el plan mensual/semanal/anual:").lower()
    estado = input("Ingrese el cliente esta activo Si / No:").lower()
    
    
    if estado == "si":
        estado = "activo"
    else:
        estado = "inactivo"

    cliente_nuevo = {
            "id":id_cliente,
            "nombre":name,
            "edad":edad,
            "plan":plan,
            "estado":estado
        }
     

    clientes.append(cliente_nuevo)

   

def buscar_cliente ():

    if not clientes:
        print("no hay clientes reguistrados" )
        return
    

    try:
        id_buscar = int(input("Ingrese el ID del cliente a Buscar: "))
        
        for cliente in clientes:
            if cliente["id"]==id_buscar:
                print("\n")
                print("="*15)
                print(f"Cliente  {cliente['nombre']}")
                print(f"Plan actual {cliente['plan']}")
                print(f"Su estado es {cliente['estado']}")
                print("="*15)
                

            


    except ValueError:

        print("Error:ingrese un valor valido")
    
def actualizar_cliente():

    cliente_update = int(input("Ingrese el ID del cliente a Actualizar : "))
    
    for cliente in clientes:

        if cliente["id"] == cliente_update:

            print(" ¿Que desea actualizar?")
            print(" 1. Plan")
            print(" 2. Estado")

            optiones_update = input("Ingrese el numero de la accion a actualizar: ")

            if optiones_update == "1":

                nuevo_plan = input("Ingrese el nuevo plan Semanal/mensual/Anual: ").lower()

                cliente["plan"] = nuevo_plan
        
            elif optiones_update == "2":

                nuevo_estado = input("Ingrese el nuevo estado Activo / Inactivo: ").lower()

                cliente["estado"] = nuevo_estado

            
            print(f"El nuevo plan de {cliente['id']} es {cliente['plan']}")
            print(f"El nuevo estado de {cliente['id']} es {cliente['estado']}")
            return

      
    print("Error: cliente no encontrado")




def eliminar_cliente():
    cliente_eliminado = int(input("Ingrese el ID del cliente a eliminar"))
    
    for cliente in clientes:
        if cliente["id"]== cliente_eliminado:
           clientes.remove(cliente)
           print(f"Cliente con el ID {cliente_eliminado} fue eliminado exitosa mente")
           return
    print("Cliente no encontado")
import json

def guardar_json():
    try:
        with open("Clientes_gym.json", "w") as archivo:
            json.dump(clientes,archivo,indent=4)
            print("datos guardados")
    except Exception as e:
        print(f"Ocurrio un error:{e}")

def cargar_json():
    global clientes
    try:
        with open("Clientes_gym.json","r") as archivo:
            clientes = json.load(archivo)
    except:
        print("No hay archivo aún, iniciando lista vacía")




