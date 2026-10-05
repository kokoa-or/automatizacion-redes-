##Topologia 2

1.	Crear un nuevo proyecto desde File\New blank Project y asignar el nombre de “MiSegundaTopologia” y pulsar “Ok”.

2.	Agregar un switch Cisco IOSvL2 y dos routers Cisco IOSv.

3.	Cablear cada router al switch: desde Gi0/0 del router 1 a Gi0/0 del switch y desde Gi0/0 del router 2 a Gi0/1 del switch.

4.	Personalizar símbolos en routers y switch, agregar etiquetas de las interfaces y renombrar el texto de los dispositivos, ajustando la vista para que se vea similar a la siguiente imagen:

 
NOTA: El switch es multicapa.

5.	Inicializar la topología y abrir la consola de los tres dispositivos de red. NOTA: Como en todos ellos debe ‘bootear’ el sistema operativo de Cisco IOS, tardará algunos minutos antes de poder empezar a configurar comandos.

 

6.	En R1, introducir los siguientes comandos, línea por línea:

Router#configure terminal
Router(config)#hostname R1
R1(config)#interface gi0/0
R1(config-if)#no shutdown
R1(config-if)#ip address 10.1.1.1 255.255.255.0
R1(config-if)#interface loopback 0
R1(config-if)#ip address 1.1.1.1 255.255.255.255
R1(config-if)#end
R1#show ip interface brief
R1#write


7.	En R2, realizar una configuración similar:

Router#configure terminal
Router(config)#hostname R2
R2(config)#interface gi0/0
R2(config-if)#no shutdown
R2(config-if)#ip address 10.1.1.2 255.255.255.0
R2(config-if)#interface loopback 0
R2(config-if)#ip address 2.2.2.2 255.255.255.255
R2(config-if)#end
R2#show ip interface brief
R2#write

Explicar el propósito de los comandos utilizados.
Router#configure terminal -Permite modificar parámetros que afectan a todo el dispositivo
Router(config)#hostname R2 -Asigna el nombre de host R1 al dispositivo
R2(config)#interface gi0/0 -Ingresa al modo de configuración específico de la interfaz física Gigabit Ethernet
R2(config-if)#no shutdown -Habilita la interfaz cambiando su estado administrativo a UP
R2(config-if)#ip address 10.1.1.2 255.255.255.0 -Asigna la dirección IPv4 10.1.1.1 con la máscara de subred /24 a la interfaz física.
R2(config-if)#interface loopback 0 -Crea e ingresa al modo de configuración de una interfaz lógica
R2(config-if)#ip address 2.2.2.2 255.255.255.255 -Asigna la dirección IPv4 1.1.1.1 con máscara /32 a la interfaz loopback
R2(config-if)#end -Sale de los modos de configuración y regresa directamente al Modo EXEC Privilegiado
R2#show ip interface brief -Muestra un resumen en tabla del estado de todas las interfaces del router
R2#write -Guarda la configuración activa en memoria RAM a la memoria no volátil NVRAM


8.	Realiza un ping entre R1 y R2 y viceversa. Comprueba que los pings sean exitosos.


9.	A continuación, en ambos routers habilitaremos OSPF como protocolo de enrutamiento. Los siguientes comandos deben ejecutarse exactamente igual tanto para R1 como para R2.

R1#configure terminal
R1(config)#router ospf 1
R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
R1(config-router)#end
R1#write

Realizar la misma configuración en R2.

10.	Ahora, apliquemos esta configuración al switch:

Switch>enable
Switch#configure terminal
Switch(config)#hostname S1
S1(config)#interface vlan 1
S1(config-if)#ip address 10.1.1.3 255.255.255.0
S1(config-if)#no shutdown
S1(config-if)#end
S1#write

NOTA: A diferencia de con las PCs, en los routers y switches se guarda la configuración con el comando write, por lo que, si realizas varias modificaciones en las configuraciones se recomienda ejecutar el comando varias veces para asegurar que se guarden los cambios.

11.	Una vez aplicadas estas configuraciones, ejecuta desde R1 y R2 el siguiente comando para validar que el protocolo OSPF está funcionando adecuadamente:

R1#show ip ospf neighbor

12.	Finalmente, en R1 ejecuta el siguiente comando para desplegar la tabla de enrutamiento:

R1#show ip route

Identificar:
•	redes conectadas;
•	rutas aprendidas;
•	rutas relacionadas con OSPF.


