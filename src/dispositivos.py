
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


def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Protocolo:", dispositivo["protocolo"])


    if dispositivo["estado"] == "Activo":
        print("El dispositivo está funcionando correctamente.")
    else:
        print("El dispositivo requiere revisión.")


for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)
    print("--------------------")


nombre_buscado = input("\nIngrese el nombre del dispositivo a buscar: ")

encontrado = False

for dispositivo in dispositivos:
    if dispositivo["nombre"].upper() == nombre_buscado.upper():
        print("\nDispositivo encontrado:")
        mostrar_dispositivo(dispositivo)
        encontrado = True
        break

if not encontrado:
    print("\nDispositivo no encontrado.")
