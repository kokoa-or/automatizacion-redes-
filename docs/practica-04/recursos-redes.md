## Recursos de GNS3 y automatización de redes ##

1. ¿Qué tipo de problema podrías resolver consultando la documentación de GNS3?

Podría resolver problemas relacionados con la creación y configuración de topologías de red, la conexión entre routers y switches virtuales, la configuración de dispositivos y la solución de errores al iniciar una simulación. También permite conocer los requisitos y las opciones de configuración de GNS3.

2. ¿Qué diferencia existe entre la documentación de una herramienta y el repositorio de una biblioteca?

La documentación de una herramienta explica cómo instalarla, configurarla y utilizar sus funciones. En cambio, el repositorio de una biblioteca contiene sus archivos de código, ejemplos, versiones y, generalmente, instrucciones para instalarla y utilizarla. También permite revisar los cambios realizados y reportar errores.

3. ¿Qué información revisarías antes de utilizar una biblioteca de automatización?

Revisaría su documentación, los requisitos de instalación, la versión de Python compatible, las dependencias necesarias, los dispositivos que admite, los protocolos que utiliza y los ejemplos de código disponibles. También comprobaría si tiene actualizaciones recientes y si cuenta con medidas de seguridad adecuadas.

4. ¿Por qué es importante comprobar qué plataformas y funciones admite una biblioteca?

Porque no todas las bibliotecas funcionan con los mismos dispositivos, sistemas operativos o versiones de software. Comprobar su compatibilidad ayuda a evitar errores de instalación y conexión, y permite elegir una herramienta que realmente funcione con los equipos que se desean administrar.

5. ¿Cómo podrían utilizarse estos recursos en las siguientes prácticas?

La documentación de GNS3 podría utilizarse para crear topologías, conectar dispositivos virtuales y comprobar su funcionamiento. La documentación de Netmiko y su repositorio podrían ayudar a desarrollar scripts en Python para conectarse a routers y switches compatibles, ejecutar comandos y automatizar tareas de administración de redes. Estos recursos permitirían comprender mejor las prácticas y resolver problemas durante su desarrollo.

# Recursos de redes y automatización

## Recurso 1: Documentación oficial de GNS3

- Nombre del recurso: GNS3 Documentation.
- URL:** https://docs.gns3.com/docs/
- Tema que aborda: Instalación, configuración, creación de topologías y uso de dispositivos virtuales en GNS3.
- Tipo de información que ofrece: Guías paso a paso, explicaciones, ejemplos y recomendaciones para utilizar el simulador.
- Utilidad para el proyecto integrador: Ayuda a construir y probar topologías de red virtuales antes de aplicar las configuraciones en equipos reales.
- Ejemplo de una situación en la que lo consultaría: Lo consultaría si necesito conectar dos routers, configurar sus interfaces y verificar la comunicación entre ellos.

## Recurso 2: Documentación oficial de Netmiko

- Nombre del recurso: Netmiko Documentation.
- URL: https://ktbyers.github.io/netmiko/
- Tema que aborda: Automatización de dispositivos de red mediante Python y conexiones SSH.
- Tipo de información que ofrece: Instrucciones de instalación, ejemplos de código, plataformas compatibles y explicaciones de las funciones de la biblioteca.
- Utilidad para el proyecto integrador: Permite desarrollar scripts que se conecten a dispositivos compatibles, ejecuten comandos y automaticen tareas de administración de redes.
- Ejemplo de una situación en la que lo consultaría: Lo utilizaría si necesito crear un programa en Python que se conecte a un router Cisco compatible y ejecute el comando `show ip interface brief` para revisar sus interfaces.

## Recurso 3: Repositorio oficial de Netmiko en GitHub

- Nombre del recurso: Netmiko GitHub Repository.
- URL: https://github.com/ktbyers/netmiko
- Tema que aborda: Código fuente, desarrollo, ejemplos, versiones y compatibilidad de la biblioteca Netmiko.
- Tipo de información que ofrece: Archivos del proyecto, instrucciones de instalación, ejemplos de uso, historial de cambios, reportes de errores y lista de plataformas compatibles.
- Utilidad para el proyecto integrador: Ayuda a comprender cómo se utiliza la biblioteca, revisar ejemplos y comprobar si los dispositivos de la práctica son compatibles antes de desarrollar un script.
- Ejemplo de una situación en la que lo consultaría: Lo consultaría para verificar si Netmiko admite el sistema operativo de un router que deseo administrar y revisar un ejemplo de conexión SSH antes de escribir mi propio programa.
