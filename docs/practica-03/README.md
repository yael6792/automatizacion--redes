# Práctica 3: Primer programa de Python para representar información de dispositivos

## 1. Propósito
Desarrollar un programa en Python capaz de estructurar, almacenar y consultar datos de dispositivos de red utilizando variables, listas, diccionarios, condicionales y funciones como paso previo a la automatización.

## 2. Conceptos utilizados
- Variables y tipos de datos
- Diccionarios (claves y valores)
- Listas de diccionarios
- Ciclos for y condicionales if/else
- Funciones y Reto Final de búsqueda

## 3. Dispositivos representados
| Dispositivo | Tipo | Dirección IP | Estado | Protocolo | Función |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R1 | Router | 10.1.1.1 | Activo | OSPF | Enrutamiento |
| R2 | Router | 10.1.1.2 | Activo | OSPF | Enrutamiento |
| S1 | Switch | 10.1.1.3 | Fuera de servicio | STP | Conectividad |

## 4. Evidencias
*(Agrega aquí las capturas de tu código, de la ejecución general y del reto de búsqueda).*

## 5. Preguntas de análisis
- **¿Por qué es útil representar la información mediante un programa?** Permite centralizar datos operativos, facilitar consultas rápidas y preparar la base para scripts de automatización.
- **¿Qué ventaja ofrece usar un diccionario?** Agrupa múltiples atributos relacionados (IP, estado, protocolo) bajo claves legibles para un solo dispositivo.
- **¿Qué ventaja ofrece usar una lista?** Permite gestionar y recorrer múltiples dispositivos de manera secuencial y ordenada.
- **¿Qué tarea realiza el ciclo for?** Itera sobre cada dispositivo de la lista para procesar o mostrar su información de forma automática.
- **¿Para qué se utilizó la estructura if?** Para evaluar condiciones lógicas, como verificar si un equipo está activo o filtrar coincidencias en la búsqueda.
- **¿Qué ventaja tiene utilizar una función?** Reutilizar bloques de código, evitar redundancia y mantener el programa modular y legible.