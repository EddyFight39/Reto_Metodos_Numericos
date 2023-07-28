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

