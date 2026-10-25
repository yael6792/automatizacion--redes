# Recursos de Redes, Simulación y Automatización

1. Preguntas de Análisis sobre Recursos de Redes

 ¿Qué tipo de problema podrías resolver consultando la documentación de GNS3?
Problemas vinculados a la infraestructura de red virtualizada y el entorno de simulación. Por ejemplo, errores al cargar o iniciar imágenes de sistemas operativos de red (Dynamips, IOU, QEMU/KVM), problemas de conectividad con el GNS3 VM, configuración de adaptadores de red de las máquinas host, y errores de enlace o topología física entre routers y switches.

 ¿Qué diferencia existe entre la documentación de una herramienta y el repositorio de una biblioteca?
* Documentación de una herramienta (como GNS3): Se orienta al funcionamiento de una plataforma de software integral, cubriendo instalación, requerimientos de hardware, uso de interfaz gráfica, emulación de dispositivos y resolución de fallos del sistema o hipervisor[cite: 1].
* Repositorio de una biblioteca (como Netmiko en GitHub): Se enfoca en el código fuente de un módulo de programación[cite: 1]. Contiene las clases, métodos y funciones para interactuar programáticamente con equipos, además del historial de versiones, problemas abiertos (Issues) y ejemplos de scripts de automatización[cite: 1].

 ¿Qué información revisarías antes de utilizar una biblioteca de automatización?
* Requisitos de instalación y dependencias necesarias.
* Versiones de Python soportadas.
* Lista de sistemas operativos y plataformas de red compatibles (Cisco IOS, Arista EOS, Juniper JunOS, etc.).
* Métodos de autenticación y cifrado admitidos (claves SSH, contraseñas, Telnet).
* Estado de mantenimiento activo del proyecto (últimos commits, versiones estables y solución de fallos).

 ¿Por qué es importante comprobar qué plataformas y funciones admite una biblioteca?
Porque los comandos, modos de configuración, manejo de prompts y respuestas varían drásticamente entre fabricantes y sistemas operativos de red[cite: 1]. Si la biblioteca no incluye el driver o soporte específico para el dispositivo con el que se trabaja, el script fallará al interpretar la sesión SSH, provocando tiempos de espera agotados (timeouts) o errores de sintaxis al enviar comandos[cite: 1].

 ¿Cómo podrían utilizarse estos recursos en las siguientes prácticas?
Servirán como base técnica para conectar scripts de Python a los routers simulados en GNS3[cite: 1]. Permitirán estructurar conexiones remotas mediante Netmiko, enviar configuraciones automáticas de interfaces, extraer tablas de ruteo y diagnosticar de forma rápida fallos de conectividad o compatibilidad durante la automatización[cite: 1].

---

 2. Recursos Técnicos Consultados

 Recurso 1
* Nombre del recurso: Documentación Oficial de GNS3 (GNS3 Documentation)
* URL: [https://docs.gns3.com/](https://docs.gns3.com/)
* Tema que aborda: Instalación, arquitectura del servidor/cliente, configuración del GNS3 VM y despliegue de appliances de red.
* Tipo de información que ofrece: Guías técnicas oficiales paso a paso, solución de problemas de virtualización y manual de referencia de la herramienta.
* Utilidad para el proyecto integrador: Ayuda a asegurar que los dispositivos de red estén correctamente configurados e interconectados para responder a las solicitudes de red.
* Ejemplo de una situación en la que lo consultaría: Cuando un router emulado no responda por consola o se requiera conectar la máquina virtual de GNS3 a la red local de la computadora para permitir el acceso por SSH.

Recurso 2
* Nombre del recurso: Repositorio Oficial de Netmiko en GitHub
* URL: [https://github.com/ktbyers/netmiko](https://github.com/ktbyers/netmiko)
* Tema que aborda: Conectividad SSH simplificada hacia dispositivos de red de múltiples fabricantes.
* Tipo de información que ofrece: Código fuente, lista oficial de plataformas soportadas (`device_type`), instrucciones de instalación, ejemplos de conexión y sección de Issues.
* Utilidad para el proyecto integrador: Permite conocer los parámetros requeridos para establecer una sesión de automatización con los equipos simulados (host, puerto, usuario, contraseña, secret).
* Ejemplo de una situación en la que lo consultaría: Para revisar el parámetro exacto de `device_type` que debe asignarse a un router Cisco IOS al crear el diccionario de conexión en Python.

 Recurso 3
* Nombre del recurso: Ejemplos y Tutoriales de Netmiko (Netmiko Examples & Documentation)
* URL: [https://ktbyers.github.io/netmiko/](https://ktbyers.github.io/netmiko/)
* Tema que aborda: Uso de métodos principales como `send_command()`, `send_config_set()` y manejo del modo enable.
* Tipo de información que ofrece: Documentación de API, guías de referencia de funciones y fragmentos de código listos para implementar.
* Utilidad para el proyecto integrador: Muestra cómo enviar comandos de visualización y configuración a los routers de manera estructurada y segura desde Python.
* Ejemplo de una situación en la que lo consultaría: Al diseñar una función para recolectar las tablas de enrutamiento o cambiar la configuración de una interfaz sin bloquear la ejecución del script.

---

3. Evidencia

A continuación se presentan las capturas de los recursos técnicos consultados:

![Evidencia 3 - Documentación de GNS3 y Netmiko](evidencias/evidencia-03-redes.png)