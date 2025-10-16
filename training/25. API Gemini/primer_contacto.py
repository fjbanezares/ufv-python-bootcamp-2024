# -*- coding: utf-8 -*-

# ¡Importamos nuestra herramienta mágica de Google!
import google.genai as genai
import os

import logging

# Añade estas líneas al principio de tu script
logging.basicConfig(level=logging.DEBUG)

# ... (el resto de tu código de genai)

# --- LA NUEVA FORMA ---
# La nueva biblioteca (google-genai) está diseñada para encontrar
# automáticamente la variable de entorno 'GOOGLE_API_KEY'.
# Por lo tanto, el bloque genai.configure() ya no es necesario
# si has configurado la variable de entorno correctamente.

# Nos aseguramos de que la variable de entorno exista.
# Si no, detenemos el programa con un mensaje claro.
if "GEMINI_API_KEY" not in os.environ:
    print("¡Error! La variable de entorno GOOGLE_API_KEY no está configurada.")
    print("Por favor, créala y asigna tu clave API.")
    exit()

try:

    #     client = genai.Client(api_key="YOUR_API_KEY")

    # response = client.models.generate_content(
    #     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    # )
    # print(response.text)
    # Creamos una instancia del modelo que queremos usar.
    # El SDK usará automáticamente la clave API de la variable de entorno.

    client = genai.Client()
    # model = genai.GenerativeModel('gemini-1.5-flash-latest')

    # ¡Y aquí vamos! Enviamos nuestro prompt al modelo.
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explica la computación cuántica como si yo fuera un pirata del siglo XVII.")

    # Imprimimos la respuesta del modelo.
    print("\nRespuesta del Capitán Gemini:")
    print("----------------------------")
    print(response.text)

except Exception as e:
    # Capturamos otros posibles errores (ej. clave API inválida)
    print(f"Ha ocurrido un error al contactar con la API de Gemini: {e}")
