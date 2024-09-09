import flet as ft
import requests
import base64
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

def main(page):
    logoPokemon = ft.Image(src = f"logo.png", width = 350, height = 170)
    nombre = ft.TextField(label = "Nombre", autofocus = True)
    submit = ft.ElevatedButton("Consultar")
    pokemonImagen = ft.Image(src = "background.png", width = 350, height = 350)

    def btn_click(e):
        urlAPI = f'https://pokeapi.co/api/v2/pokemon/{nombre.value}'
        result = requests.get(urlAPI)

        if result.status_code == 200:
            pokemonData = result.json()
            urlImagen = pokemonData['sprites']['other']['official-artwork']['front_default']
            im = Image.open(urlopen(urlImagen))
            buffer = BytesIO()
            im.save(buffer, format = "png")
            imagenBase64 = base64.b64encode(buffer.getvalue()).decode()
            pokemonImagen.src_base64 = imagenBase64
            pokemonImagen.update()
    
    submit.on_click = btn_click
    page.add(logoPokemon, nombre, submit, pokemonImagen)

ft.app(target = main)