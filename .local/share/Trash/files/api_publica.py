import requests
import urllib.parse

# Configuración inicial
route_url = "https://graphhopper.com/api/1/route?"
key = "abaa733d-0f84-41c8-ac3b-62019ac28cd6"

while True:
    print("\n--- Calculadora de Viajes ---")
    # Solicitar “Ciudad de Origen” y “Ciudad de Destino” 
    # Agregar una salida del programa con la letra “q” 
    origen = input("Ingrese Ciudad de Origen (o 'q' para salir): ")
    if origen.lower() == 'q':
        print("Saliendo del programa...")
        break
    
    destino = input("Ingrese Ciudad de Destino (o 'q' para salir): ")
    if destino.lower() == 'q':
        print("Saliendo del programa...")
        break

    # Construir URL
    url = route_url + urllib.parse.urlencode({"point": [origen, destino], "vehicle": "car", "locale": "es", "key": key})
    
    # Realizar petición
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        paths = data["paths"][0]
        
        # Medir la distancia en kilómetros 
        distancia_km = paths["distance"] / 1000
        
        # Mostrar la duración del viaje en horas, minutos y segundos 
        tiempo_ms = paths["time"]
        segundos_totales = int(tiempo_ms / 1000)
        horas = segundos_totales // 3600
        minutos = (segundos_totales % 3600) // 60
        segundos = segundos_totales % 60
        
        # Mostrar el combustible requerido para el viaje representado en litros 
        # Asumiendo un rendimiento promedio de 12 km/litro
        litros_combustible = distancia_km / 12
        
        # Todos los valores deben utilizar dos decimales e imprimir la narrativa del viaje 
        print(f"\nNarrativa del viaje de {origen} a {destino}:")
        print(f"Distancia total: {distancia_km:.2f} km")
        print(f"Duración estimada: {horas} horas, {minutos} minutos y {segundos} segundos")
        print(f"Combustible requerido: {litros_combustible:.2f} litros")
    else:
        print("Error en la consulta. Verifique los nombres de las ciudades o su Token.")