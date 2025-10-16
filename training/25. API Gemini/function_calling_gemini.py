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

# --- Ejemplo 3: Function Calling Automático ---

# 1. Definimos una función de Python normal.
# Es importante que tenga un docstring claro y anotaciones de tipo.
# El modelo usará esta información para entender qué hace la función.


def obtener_temperatura_actual(ciudad: str) -> str:
    """Obtiene la temperatura actual para una ciudad específica."""
    # En una aplicación real, aquí llamarías a una API meteorológica.
    # Para este ejemplo, simulamos la respuesta.
    if "madrid" in ciudad.lower():
        return "La temperatura en Madrid es de 25°C con sol."
    elif "londres" in ciudad.lower():
        return "La temperatura en Londres es de 18°C y está nublado."
    else:
        return f"No tengo datos del tiempo para {ciudad}."


# 2. Hacemos la petición al modelo.
prompt = "¿Qué temperatura hace en Madrid?"

# En la configuración, pasamos la función directamente en la lista de 'tools'.
# El SDK se encarga de todo el proceso de forma automática.
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        tools=[obtener_temperatura_actual]  # ¡Así de fácil!
    )
)

print(f"Pregunta: {prompt}")
print(f"Respuesta del modelo: {response.text}")
