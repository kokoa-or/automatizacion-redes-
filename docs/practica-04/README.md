# Propósito de la práctica

El propósito de esta práctica es identificar, consultar y evaluar diferentes recursos de documentación y comunidades de colaboración relacionados con Python, GNS3 y la automatización de redes. También se busca aprender a seleccionar información confiable y organizarla para utilizarla posteriormente en el proyecto integrador.

# Relación con el proyecto integrador

Los recursos investigados servirán como apoyo durante el desarrollo de los programas de automatización de redes. La documentación de Python permitirá resolver dudas relacionadas con el lenguaje y sus bibliotecas, mientras que la documentación de GNS3 y otros recursos de redes ayudarán a comprender y solucionar problemas relacionados con la infraestructura y la automatización.

# Recursos consultados

Se consultó la documentación oficial de Python, la documentación de GNS3 y la comunidad Stack Overflow. Estos recursos permiten encontrar información técnica, ejemplos, instrucciones y posibles soluciones a problemas relacionados con programación y redes.

Documentacion Oficial de Pyhton: 
https://docs.python.org/es/3/
Esta página contiene la documentación oficial de Python en español. Explica el funcionamiento del lenguaje, sus estructuras de datos, funciones, módulos y otras características. La consultamos para resolver dudas al desarrollar el programa dispositivos.py, especialmente si necesitamos trabajar con listas, diccionarios, ciclos o búsquedas de dispositivos.

Documentacion oficial GNS3:
https://docs.gns3.com/docs/
Este sitio contiene guías e información sobre el uso de GNS3, la creación de topologías y la configuración del entorno de simulación de redes. Lo utilizamos para comprender mejor la infraestructura de red simulada y consultar procedimientos cuando se presenten problemas durante las siguientes prácticas.

Stack Overflow:
https://es.stackoverflow.com/
Es una comunidad donde los usuarios publican preguntas y respuestas relacionadas con programación. Permite consultar problemas que otros desarrolladores han encontrado y conocer posibles soluciones. Buscamos información sobre cómo localizar un dispositivo por su nombre en Python.

GitHub:
https://github.com/search?q=python+network+automation&type=repositories
Consultamos repositorios relacionados con Python y la automatización de redes para conocer cómo otros desarrolladores organizan sus proyectos, archivos y documentación. Este recurso nos sirve como referencia para mejorar la estructura de nuestro proyecto integrador y conocer ejemplos de código que puedan ayudarnos a comprender cómo se desarrollan soluciones de automatización.

Netmiko:
https://github.com/ktbyers/netmiko
Revisamos el repositorio de Netmiko para conocer una biblioteca de Python utilizada para facilitar la conexión y administración de dispositivos de red compatibles. Este recurso nos permite consultar su documentación, ejemplos de uso y plataformas admitidas. Consideramos que puede ser útil en futuras prácticas si necesitamos desarrollar programas que automaticen tareas de administración de dispositivos de red.


# Evaluacion de confiabilidada:

|Criterio | Recurso 1: Documentación oficial de Python | Recurso 2: Documentación de GNS3 | Recurso 3: Stack Overflow|
| :--- | :--- | :--- | :--- |
|**¿Quién publica o mantiene el recurso?**	|Python Software Foundation y colaboradores de Python.	|Equipo y comunidad de GNS3.	|Comunidad de usuarios y desarrolladores de Stack Overflow.|
|**¿La información corresponde al tema investigado?**	|Sí, contiene información sobre Python, sus funciones, estructuras y bibliotecas.	|Sí, proporciona información relacionada con GNS3, redes y simulación.	|Sí, contiene preguntas y respuestas sobre programación y resolución de problemas.|
|**¿Incluye ejemplos o instrucciones verificables?**	|Sí, incluye ejemplos de código y explicaciones.	|Sí, incluye instrucciones y ejemplos relacionados con el uso de GNS3.	|Sí, muchas respuestas incluyen código y procedimientos que pueden probarse.|
|**¿Se identifica la versión o fecha de actualización cuando corresponde?**	|Sí, la documentación está organizada por versiones de Python.	|Sí, la documentación se relaciona con las versiones de GNS3.	|Depende de cada publicación; se pueden consultar fechas y respuestas.|
|**¿Es posible comprobar la información con otra fuente?**	|Sí, mediante otros recursos y documentación de Python.	|Sí, mediante documentación adicional y comunidades de redes.	|Sí, comparando la respuesta con documentación oficial.|
|**¿Qué utilidad tiene para el proyecto integrador?**	|Ayuda a desarrollar y corregir los programas en Python.	|Ayuda a comprender y solucionar problemas de la infraestructura simulada.	|Permite encontrar experiencias y posibles soluciones a problemas específicos.|

1. **¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?**
La documentación oficial de Python es la más útil porque proporciona información confiable y detallada sobre el lenguaje, sus funciones, estructuras de datos y bibliotecas. Además, permite comprobar que la información corresponde a la versión utilizada.

2. **¿Cuál consultarías para resolver un problema relacionado con GNS3?**
Consultaría principalmente la documentación oficial de GNS3, porque está enfocada directamente en la configuración, funcionamiento y solución de problemas relacionados con la herramienta.

3. **¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?**
Porque una solución puede depender de una versión específica, configuración, sistema operativo o herramientas diferentes. Es necesario probarla y verificar que sea compatible con nuestro proyecto antes de incorporarla.


# Estrategia de solucion del problema

|**Elemento** | Respuesta del equipo|
| :--- | :--- | :--- | :--- |
|**Problema identificado** | El programa dispositivos.py muestra correctamente la información de los dispositivos, pero no logra identificar un dispositivo cuando se realiza una búsqueda por nombre.|
|**Palabras clave para realizar la búsqueda** | Python buscar dispositivo por nombre, búsqueda en listas y diccionarios Python, comparar cadenas, búsqueda de claves en diccionario.|
|**Documentación o comunidad que consultarían primero** | Primero consultaríamos la documentación oficial de Python y posteriormente una comunidad como Stack Overflow si la documentación no fuera suficiente.|
|**Información que revisarían en el código** | Revisaríamos cómo están almacenados los dispositivos, la variable utilizada para realizar la búsqueda, las condiciones if, las comparaciones de nombres y las funciones utilizadas para localizar el dispositivo.|
|**Tipo de ejemplo o solución que buscarían** | Buscaríamos ejemplos de búsqueda de elementos en listas o diccionarios y comparación de cadenas en Python.|
|**Cómo comprobarían que la solución funciona** | Realizaríamos pruebas buscando los dispositivos R1 y R2, además de un nombre que no exista, para verificar que el programa encuentre correctamente los dispositivos y maneje los casos inexistentes.|

# Apredizajes Obtenidos
Durante la práctica aprendimos que no todas las fuentes de información tienen el mismo nivel de confiabilidad. Es importante identificar quién mantiene un recurso, comprobar que la información sea actual y verificar las soluciones antes de utilizarlas. También aprendimos que las comunidades de colaboración pueden complementar la documentación oficial cuando se presenta un problema específico.


# Conclusion Individual

**Conclusión Ximena Elizabeth Contreras Perez**
En esta práctica aprendí que la documentación oficial es importante para comprender cómo funcionan los lenguajes de programación y las herramientas tecnológicas. También entendí que las comunidades de colaboración permiten encontrar respuestas a problemas que otros desarrolladores ya han enfrentado. Para saber si una fuente es confiable, es necesario revisar quién la publica, si está actualizada y si contiene ejemplos que podamos comprobar. En caso de tener un problema con Python, podría consultar la documentación oficial o buscar una solución en Stack Overflow. Sin embargo, no debemos copiar directamente cualquier respuesta sin verificar que funcione. También aprendí que guardar la información en GitHub facilita que otros integrantes del equipo puedan consultarla. Estos conocimientos me ayudarán a resolver problemas de manera más organizada en las siguientes prácticas.

**Conclusión Karyme De la O Rodriguez**
Durante el desarrollo de esta práctica comprendí que investigar correctamente es una parte importante de la programación. La documentación oficial ofrece información sobre el uso de las herramientas, mientras que las comunidades presentan preguntas, experiencias y soluciones de otros usuarios. Para identificar un recurso confiable, debemos revisar su origen, la fecha de actualización y la relación que tiene con el problema que queremos resolver. Si tuviera una dificultad con un programa en Python, buscaría ejemplos similares y compararía las respuestas con la documentación oficial. Después realizaría pruebas para confirmar que la solución sea adecuada. También considero importante registrar los resultados en GitHub, ya que permite mantener organizada la información del proyecto. En las siguientes prácticas utilizaré estos recursos para aprender y solucionar errores de manera más eficiente.

**Conclusión Mariana Hernandez Martinez**
Esta práctica me permitió conocer diferentes recursos que pueden ayudarnos durante el desarrollo de un proyecto de automatización de redes. Aprendí que la documentación oficial de Python y GNS3 proporciona información específica sobre sus funciones y configuraciones. Por otro lado, las comunidades de colaboración permiten consultar dudas y conocer diferentes formas de resolver un mismo problema. Para confiar en una respuesta, es necesario comprobar que sea correcta, actual y compatible con las herramientas que utilizamos. En caso de tener un error en el programa de dispositivos, buscaría información relacionada con el código y probaría diferentes casos para verificar la solución. Además, documentar los resultados en GitHub ayuda a conservar los conocimientos adquiridos. Considero que aplicar estas prácticas facilitará el trabajo en equipo y el desarrollo de futuras actividades.

**Conclusión Joseline Martinez Marin**
Al realizar esta práctica aprendí la importancia de utilizar fuentes confiables al investigar problemas relacionados con programación y redes. La documentación oficial permite consultar información detallada, mientras que los foros y comunidades ayudan a encontrar soluciones basadas en experiencias de otros usuarios. Para evaluar una fuente, revisaría quién la mantiene, si explica claramente el procedimiento y si la información puede comprobarse con otros recursos. Si encontrara un error en Python, primero investigaría su posible causa y después buscaría ejemplos que me ayudaran a comprender cómo solucionarlo. No utilizaría una solución sin probarla previamente en mi entorno de trabajo. También aprendí que GitHub puede utilizarse para almacenar código y organizar documentación útil para el equipo. En las siguientes prácticas aplicaré lo aprendido para investigar, verificar y registrar las soluciones que encontremos durante el proyecto integrador.