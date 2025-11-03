import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# Inicializar cliente OpenAI (requiere tu API key)
client = OpenAI(api_key="TU_API_KEY_AQUI")

# Inicializar motor de voz
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # velocidad de voz
engine.setProperty("volume", 1.0)

def hablar(texto):
    """Convierte texto en voz."""
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    """Escucha desde el micrófono y devuelve texto."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Escuchando...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-ES")
        print(f"Tú dijiste: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No entendí lo que dijiste.")
        return ""
    except sr.RequestError:
        print("Error con el servicio de reconocimiento.")
        return ""

def responder(pregunta):
    """Envía la pregunta a OpenAI y devuelve la respuesta."""
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente amable y útil."},
            {"role": "user", "content": pregunta}
        ]
    )
    return respuesta.choices[0].message.content

# Bucle principal
if __name__ == "__main__":
    hablar("Hola, soy tu asistente. ¿En qué puedo ayudarte?")
    while True:
        texto = escuchar()
        if texto.lower() in ["salir", "adiós", "chao"]:
            hablar("Hasta luego.")
            break
        elif texto:
            respuesta = responder(texto)
            print("🤖:", respuesta)
            hablar(respuesta)
