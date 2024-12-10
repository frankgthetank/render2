import geopandas as gpd
from dash import Dash, html
import dash_leaflet as dl
import json

# Leer el archivo .gpkg
def load_data(gpkg_path, layer_name=None):
    """
    Carga datos de un archivo .gpkg y devuelve un GeoJSON.
    """
    gdf = gpd.read_file(gpkg_path, layer=layer_name)
    gdf = gdf.to_crs(epsg=4326)  # Convertir a WGS84 (CRS compatible con Leaflet)
    return json.loads(gdf.to_json())

# Ruta al archivo .gpkg
gpkg_path = "sectores_anonimizados 1.gpkg"  # Coloca el archivo en una carpeta llamada "data"
geojson_data = load_data(gpkg_path)

# Crear la aplicación Dash
app = Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),  # Capa base
        dl.GeoJSON(data=geojson_data,  # GeoJSON cargado
                   options={"style": {"color": "blue", "weight": 2}},
                   id="geojson-layer"),
    ], style={'width': '100%', 'height': '500px'}, center=(0, 0), zoom=2)
])

# Servidor para Render
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
