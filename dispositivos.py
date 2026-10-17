# ==========================================================
# Práctica 3: Representación de información de dispositivos
# ==========================================================

# Lista de dispositivos que representa la infraestructura de red
dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "loopback": "1.1.1.1",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "loopback": "2.2.2.2",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "interfaz": "Vlan1",
        "estado": "Fuera de servicio",  # Se usa para validar la condicional de estado
        "fabricante": "Cisco",
        "protocolo": "STP"
    }
]

# Función para mostrar los datos de un dispositivo individual
def mostrar_dispositivo(dispositivo):
    print(f"Nombre: {dispositivo['nombre']}")
    print(f"Tipo: {dispositivo['tipo']}")
    print(f"Dirección IP: {dispositivo['ip']}")
    if "loopback" in dispositivo:
        print(f"Loopback: {dispositivo['loopback']}")
    print(f"Interfaz: {dispositivo['interfaz']}")
    print(f"Fabricante: {dispositivo['fabricante']}")
    print(f"Protocolo: {dispositivo['protocolo']}")
    print(f"Estado: {dispositivo['estado']}")
    
    # Condición de estado requerida
    if dispositivo["estado"] == "Activo":
        print("Diagnóstico: El dispositivo está disponible.")
    else:
        print("Diagnóstico: El dispositivo requiere atención.")

# Función para el Reto Final: Búsqueda por nombre
def buscar_dispositivo(nombre_buscar):
    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == nombre_buscar.lower():
            return dispositivo
    return None

# Recorrido general de la lista
print("=" * 45)
print("  REPORTE DE INFRAESTRUCTURA DE RED")
print("=" * 45)
for disp in dispositivos:
    mostrar_dispositivo(disp)
    print("-" * 30)

# Ejecución del Reto Final
print("\n" + "=" * 45)
print("  RETO FINAL: BUSCADOR DE DISPOSITIVOS")
print("=" * 45)
busqueda = input("Ingrese el nombre del dispositivo a buscar (ej. R1, R2, S1): ")
resultado = buscar_dispositivo(busqueda)

if resultado:
    print("\n[+] Dispositivo encontrado:")
    mostrar_dispositivo(resultado)
else:
    print(f"\n[-] El dispositivo '{busqueda}' no existe en el registro.")