import os
from google import genai
from google.genai import types

# NOTA: La forma más segura de gestionar tu API Key es a través de variables de entorno.
# Descomenta la siguiente línea si tienes tu clave guardada en una variable de entorno.
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# O, para una prueba rápida, reemplaza 'YOUR_API_KEY' con tu clave.
# ¡No subas este código con tu clave a repositorios públicos!
# Este código muestra cómo generar texto y recibir la respuesta en tiempo real (streaming),
# en lugar de esperar a que se complete toda la generación.
# Es ideal para crear una experiencia de usuario tipo chatbot.
client = genai.Client()

# Describir una Imagen Local ---

# ¡IMPORTANTE! Reemplaza esta ruta con la ruta a una imagen en tu ordenador.
ruta_imagen = "training/25. API Gemini/cuadrociguenamaria.jpg"
mime_type_imagen = "image/jpeg"  # Cambia a "image/png" si es un archivo PNG.

try:
    # Abrimos el archivo de la imagen en modo de lectura binaria ('rb').
    with open(ruta_imagen, 'rb') as f:
        imagen_bytes = f.read()

    # Creamos un objeto 'Part' a partir de los bytes de la imagen.
    # Este es el formato que el SDK necesita para procesar archivos.
    parte_imagen = types.Part.from_bytes(
        data=imagen_bytes, mime_type=mime_type_imagen)

    # El prompt consta de texto y la imagen. El SDK los combina en una sola petición.
    prompt_multimodal = [
        "Describe lo que ves en esta imagen de forma detallada.", parte_imagen]

    # Hacemos la llamada a la API con el contenido multimodal.
    response = client.models.generate_content(
        # Un modelo más potente para análisis de imagen.
        model='gemini-2.5-pro',
        contents=prompt_multimodal
    )

    print("Descripción de la imagen:")
    print(response.text)

except FileNotFoundError:
    print(
        f"Error: No se encontró el archivo en la ruta '{ruta_imagen}'. Por favor, verifica la ruta.")
