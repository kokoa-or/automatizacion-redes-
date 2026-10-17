# INVENTARIO DE DISPOSITIVOS DE RED

# Este programa almacena informacion de dispositivos de red utilizando una lista de diccionarios.
# Tambien como reto final permite mostrar informacion detallada y buscar dispositivos por su nombre.


# Lista que almacena los dispositivos de red
# Cada dispositivo se representa mediante un diccionario.
dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo"
    }
]

# FUNCION: mostrar_dispositivo()
# Recibe un dispositivo como parametro y muestra toda su informacion en pantalla.
# Ademas evalua el estado del dispositivo utilizando una estructura condicional if/else.
def mostrar_dispositivo(dispositivo):
    # Mostrar datos generales
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Protocolo:", dispositivo["protocolo"])

    # Verificar si el dispositivo está activo
    if dispositivo["estado"] == "Activo":
        print("El dispositivo está funcionando correctamente.")
    else:
        print("El dispositivo requiere revisión.")

# MOSTRAR TODOS LOS DISPOSITIVOS
# Se recorre la lista utilizando un ciclo for y se utiliza la funcion para mostrar cada dispositivo.
for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)
    print("--------------------")

# RETO FINAL: BUSQUEDA DE DISPOSITIVOS POR NOMBRE
# Se solicita al usuario el nombre de un dispositivo y el programa recorre la lista y busca coincidencias.
nombre_buscado = input("\nIngrese el nombre del dispositivo a buscar: ")

# Variable para determinar si el dispositivo fue encontrado
encontrado = False

# Recorrer la lista de dispositivos
for dispositivo in dispositivos:
        # Comparar nombres sin importar mayusculas o minusculas
    if dispositivo["nombre"].upper() == nombre_buscado.upper():
        print("\nDispositivo encontrado:")
        # Mostrar información completa del dispositivo
        mostrar_dispositivo(dispositivo)
        encontrado = True
        # Finalizar la búsqueda
        break

# Si no se encontro ningun dispositivo
if not encontrado:
    print("\nDispositivo no encontrado.")
