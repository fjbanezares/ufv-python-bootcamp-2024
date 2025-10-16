from pydantic import BaseModel
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

# Salida en JSON Estructurado ---
# Necesitarás instalar Pydantic: pip install pydantic


# 1. Definimos la estructura de datos que esperamos con Pydantic.
# Esto sirve como el "esquema" para el modelo.

class Receta(BaseModel):
    nombre_plato: str
    tiempo_preparacion_min: int
    ingredientes: list[str]
    dificultad: str


prompt = "Dame una receta sencilla para hacer una tortilla de patatas."

# 2. Hacemos la llamada a la API especificando el formato de salida.
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Le decimos al modelo que la respuesta DEBE ser JSON.
        response_mime_type='application/json',
        # Le pasamos nuestra clase de Pydantic como el esquema a seguir.
        response_schema=Receta,
    )
)

print("Prompt:", prompt)
print("\nRespuesta en formato JSON:")
print(response.text)

# Puedes convertir fácilmente el texto JSON en un objeto Pydantic
try:
    receta_obj = Receta.model_validate_json(response.text)
    print("\nObjeto Pydantic validado:")
    print(f"Plato: {receta_obj.nombre_plato}")
    print(f"Dificultad: {receta_obj.dificultad}")
except Exception as e:
    print(f"\nError al validar el JSON: {e}")
