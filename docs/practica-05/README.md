## Practica 5
**Objetivo**
Se creara una topología de red en GNS3 y se configurara un script de automatización utilizando Python para aplicar configuraciones vía Telnet a un router. Esta práctica da continuidad al proyecto integrador “Sistema de automatización y gestión de infraestructura de red”: parte de la topología construida en prácticas previas, aprovecha los conocimientos de Python y los recursos investigados, y agrega la primera interacción automatizada con un dispositivo. Los pasos numerados y las imágenes del procedimiento se presentan más adelante en este documento.

En las prácticas 1 a 4 se preparó el entorno de trabajo, se construyó una infraestructura simulada en GNS3, se representó información de dispositivos con Python y se exploraron recursos técnicos. En esta Práctica 5, el programa comenzará a interactuar con un router de laboratorio para enviar configuraciones y comprobar sus resultados.

**Topologia**
Importar Network Automation Container
Ethernet switch.
NAT Cloud
Switch de capa 2 Cisco IOSvL2
Router Cisco IOSv 

Version de python: 3.10

**Explicación del script**
El código utiliza Python para conectarse al router R1 mediante el protocolo Telnet y realizar configuraciones de manera automática. Primero, importa las librerías getpass y telnetlib, que permiten solicitar la contraseña de forma segura y establecer la conexión con el router.

Después, se define la dirección IP del router mediante la variable HOST y se solicitan el nombre de usuario y la contraseña para ingresar. Una vez establecida la conexión, el programa envía los datos de acceso y utiliza el comando enable para entrar al modo privilegiado.

Posteriormente, el programa ejecuta configure terminal para comenzar a modificar la configuración del router. Primero configura la interfaz Loopback0 con la dirección IP 1.1.1.1 y la máscara 255.255.255.255. Después, crea la interfaz Loopback1 y le asigna la dirección IP 2.2.2.2 con la misma máscara.

A continuación, configura el protocolo de enrutamiento OSPF mediante el comando router ospf 1. Después utiliza el comando network 0.0.0.0 255.255.255.255 area 0 para incluir todas las interfaces IPv4 que coincidan con esa dirección y máscara dentro del área 0.

Finalmente, el comando end termina la configuración y print(tn.read_all().decode('ascii')) muestra la información recibida del router en la consola.

En general, este código permite automatizar la configuración del router R1 utilizando Python, agregando una interfaz Loopback y habilitando OSPF sin necesidad de introducir todos los comandos manualmente.

*Tabla de pruebas, problemas y soluciones*
Durante la practica no hubo problemas con las verificaciones o con versiones de python
 
**Conclusiones**
Ximena
En esta actividad aprendí a configurar un router utilizando Python y el protocolo Telnet.
También comprendí cómo un programa puede enviar comandos automáticamente a un dispositivo de red. Esto permite realizar configuraciones sin tener que escribir cada comando manualmente. Además, conocí la importancia de utilizar correctamente las credenciales para acceder al router. Considero que esta herramienta facilita el trabajo y ahorra tiempo al administrar redes.

Mariana
Aprendí a crear una nueva interfaz Loopback en el router R1 y asignarle una dirección IP.
La interfaz Loopback es virtual y permite realizar pruebas y configuraciones de red.
En esta actividad se agregó la Loopback1 con la dirección IP 2.2.2.2.
También comprendí que cada interfaz necesita una dirección IP y una máscara de subred.
Esto me ayudó a entender mejor cómo se identifican las interfaces dentro de un router.

Karyme
Durante la actividad aprendí a hacer un script.
Tambien que el protocolo OSPF permite que los routers compartan información para encontrar rutas dentro de una red.  Mediante el comando network se pueden indicar las interfaces que participarán en el protocolo. Esto es importante porque ayuda a mantener una comunicación adecuada entre los dispositivos de red.

Joseline
Esta práctica me permitió relacionar los conocimientos de Python con la administración de redes. Comprendí que la automatización ayuda a realizar tareas de configuración de manera más rápida y sencilla. También aprendí que es importante verificar que los cambios se hayan aplicado correctamente en el router. Los comandos de consulta permiten revisar las direcciones IP y el funcionamiento de OSPF. Finalmente, considero que estas herramientas son útiles para mejorar la administración y el mantenimiento de las redes.
