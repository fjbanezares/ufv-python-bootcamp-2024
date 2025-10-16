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

# --- Ejemplo 1: Generación de Texto con Streaming ---

# El prompt o la pregunta que le haremos al modelo.
prompt = "Escribe un poema corto sobre la luna y las estrellas."

print(f"Pregunta: {prompt}\nRespuesta: ")

# Usamos 'generate_content_stream' para obtener la respuesta en fragmentos (chunks).
# Esto permite mostrar el texto a medida que se genera.
stream = client.models.generate_content_stream(
    model='gemini-2.5-flash',  # Usamos un modelo rápido y eficiente.
    contents=prompt
)

# Iteramos sobre cada fragmento de la respuesta que llega.
for chunk in stream:
    # Imprimimos el texto del fragmento sin saltar de línea para que aparezca seguido.
    print(chunk.text, end="")

print("\n--- Fin del Stream ---")
