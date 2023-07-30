import geocoder
import folium

def obtener_posicion_actual():
    g = geocoder.ip('me')
    return g.latlng

# Obtener la posición actual
posicion_actual = obtener_posicion_actual()
print(f"La posición actual es: {posicion_actual}")

# Crear un mapa utilizando folium
mapa = folium.Map(location=posicion_actual, zoom_start=10)

# Agregar un marcador en la posición actual
folium.Marker(posicion_actual, popup="Posición actual").add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapa.html")

# Abrir el archivo HTML en el navegador
import webbrowser
webbrowser.open("mapa.html")




#VERSION 2

import folium

def obtener_coordenadas():
    coordenadas_str = input("Ingresa las coordenadas (latitud, longitud): ")
    lat_str, lng_str = coordenadas_str.split(',')
    lat = float(lat_str.strip())
    lng = float(lng_str.strip())
    return lat, lng

def crear_mapa(posicion_actual):
    print(f"La posición ingresada es: {posicion_actual}")

    # Crear un mapa utilizando folium
    mapa = folium.Map(location=posicion_actual, zoom_start=10)

    # Agregar un marcador en la posición actual
    folium.Marker(posicion_actual, popup="Posición actual").add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save("mapa.html")

    # Abrir el archivo HTML en el navegador
    import webbrowser
    webbrowser.open("mapa.html")

if __name__ == "__main__":
    # Obtener la posición actual ingresando las coordenadas
    lat, lng = obtener_coordenadas()
    posicion_actual = (lat, lng)

    # Crear el mapa
    crear_mapa(posicion_actual)

