# send_email.py
import os
import resend

resend.api_key = os.environ["RESEND_API_KEY"]


def enviar_email(destinatario, asunto, cuerpo):
    return resend.Emails.send({
        "from": os.environ["FROM_EMAIL"],
        "to": [destinatario],
        "subject": asunto,
        "text": cuerpo
    })


# Test
if __name__ == "__main__":
    resp = enviar_email("usuario@example.com",
                        "Hola desde Resend", "Este es un correo de prueba")
    print(resp)
