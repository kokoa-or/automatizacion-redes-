##Topologia 1

1.	Abrir GNS3 GUI, esperar a que carguen, desde el panel derecho “Servers Summary” tanto el servidor local como la máquina virtual.

2.	Crear nuevo proyecto desde la ventana que aparece en el centro, asignando un nombre tal como: “MiPrimeraTopologia” y hacer clic en “Ok”.

3.	Colocar un switch y dos computadoras y conectarlos entre sí:
a.	Desde el botón “Browse Switches” del panel lateral izquierdo  , arrastrar y soltar en el área de trabajo un “Ethernet switch”. Al soltar el dispositivo en el área de trabajo se te preguntará en qué servidor deseas guardar el dispositivo: selecciona GNS3 VM.

NOTA: A menos que se indique lo contrario, todos los dispositivos se guardarán en GNS3 VM, de acuerdo con la configuración establecida durante la Práctica 1.

b.	Desde el botón “Browse End Devices”   arrastrar y soltar dos computadoras: VPCS.

c.	Usando el botón “Add a link” unir el puerto Ethernet0 desde PC1 al puerto Ethernet0 del switch y del puerto Ethernet1 al Ethernet0 de PC2. Presionar Esc para ya no usar la herramienta de agregar link; el puntero del mouse regresará al predeterminado.

d.	Mostrar las etiquetas de las interfaces usando el botón “Show/Hide interface labels” de la barra de herramientas.

e.	Cambiar los símbolos de las PCs y del switch haciendo clic derecho sobre el dispositivo y usando la opción “Change symbol” del menú contextual. Para las PCs busca el icono de client desde la categoría “Affinity-circle-blue” y el de switch en la categoría “Affinity-square-blue”

f.	Ajustar la vista del programa, desde View\Fit in view. Tu entorno debería ser similar al siguiente:

 
4.	Inicializar la topología mediante el botón “Start/Resume all nodes”   de la barra de herramientas. Confirmar (“Yes”) en la caja de diálogo que aparecerá. Podrás observar que los leds que indican conectividad de red cambiarán todos a color verde.

5.	Ahora vamos a configurar una IP a cada PC. Para ello, usaremos la consola. Sobre el icono de PC1 hacer clic derecho y seleccionar “Console”. Abrir también la consola de PC2.

a.	En PC1, ejecutar el comando:
> ip 10.1.1.1 255.255.255.0
> save

b.	En PC2, ejecutar el comando:
> ip 10.1.1.2 255.255.255.0
> save

NOTA: En GNS3, a diferencia de otras opciones de software simulador como Cisco Packet Tracer, las configuraciones no se guardan automáticamente, razón por la cual, podrás observar el comando “save” que se ejecutó en cada PC.

c.	Realiza un ping para comprobar conectividad desde PC1 a PC2 y viceversa.

6.	Detener la topología  . Confirmar.
