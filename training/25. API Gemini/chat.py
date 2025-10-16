# -*- coding: utf-8 -*-
import google.genai as genai
import os

import logging

# Añade estas líneas al principio de tu script
logging.basicConfig(level=logging.DEBUG)

# Nos aseguramos de que la variable de entorno exista.
if "GEMINI_API_KEY" not in os.environ:
    print("¡Error! La variable de entorno GEMINI_API_KEY no está configurada.")
    exit()

try:
    # 1. Creamos el cliente, que usará la clave API del entorno.
    client = genai.Client()

    # 2. Creamos una lista vacía para guardar el historial de la conversación.
    #    Nosotros seremos los responsables de gestionarla.
    chat_history = []

    print("¡Bienvenido al Chatbot de Gemini! Escribe 'salir' para terminar.")
    print("------------------------------------------------------------")

    # Un bucle infinito para mantener la conversación viva.
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("¡Hasta la próxima, explorador de IA!")
            break

        # 3. Añadimos el mensaje del usuario al historial.
        chat_history.append({'role': 'user', 'parts': [{'text': user_input}]})

        # 4. Enviamos la conversación COMPLETA al modelo.
        #    La clave está en pasar toda la lista 'chat_history' en el parámetro 'contents'.
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # Usamos un modelo actual y rápido
            contents=chat_history
        )

        # Extraemos el texto de la respuesta del modelo.
        model_response_text = response.text
        print(f"Gemini: {model_response_text}")

        # 5. ¡Importante! Añadimos la respuesta del modelo al historial
        #    para que tenga el contexto en el siguiente turno.
        chat_history.append(
            {'role': 'model', 'parts': [{'text': model_response_text}]})

    # (Opcional) Mostramos el historial final que hemos construido.
    print("\n--- Historial de la Conversación ---")
    for message in chat_history:
        print(f"**{message['role']}**: {message['parts'][0]['text']}")

except Exception as e:
    # Capturamos otros posibles errores (ej. clave API inválida)
    print(f"Ha ocurrido un error al contactar con la API de Gemini: {e}")
