import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, me estaba fajando con un verde. En qué puedo ayudar?.")

# Función para manejar mensajes con palabras clave
async def respond_to_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()  # Convertir el mensaje a minúsculas para evitar problemas de mayúsculas/minúsculas
    
    # Diccionario de palabras clave y sus respuestas
    keyword_responses = {
        "verde": "Del castillo verde, nadie se acuerda, pero en los torneos, el rey en calzones siempre vuelve.",  # Sustituye con la palabra clave y su respuesta
        "azul": "Del castillo azul, el caballero que decía ser tan cool, se cayó del burro y se rompió el cucul.",  # Puedes añadir más palabras clave y respuestas
        "rojo": "En el castillo rojo, la cosa está floja, todos se rascan y ninguno se moja. Dicen que el rey siempre tiene antojo, pero cuando lo buscan, lo pillan cojo.",
        "amarillo": "💪",
        "beso": "Un beso en la boca, y no quiero más, pero si me das un trago, ¡que empiece el desmadre ya!",
        "sexo": "El sexo es un arte, lo digo sin pudor, pero si no hay química, ¡mejor ve a dormir, amor!",
        "cerveza": "La cerveza fría es lo mejor para brindar, pero si tomas de más, ¡te vas a vomitar!",
        "juguete": "El juguete en la caja, siempre listo para el juego, pero si no hay pilas, ¡te quedas sin el fuego!",
        "baño": "En el baño me encerré, pensando en mi placer, pero al ver que no había papel, ¡me quedé en apuro al querer!",
        "cinco": "Por el culo te la hinco",
        "13": "Mmmmm",
        "vino": "En tu culo mi pepino",
        "pedro": "Hola, me estaba fajando con un verde. En qué puedo ayudar?"
    }

    # Comprobar si alguna palabra clave está contenida dentro del mensaje
    for keyword, response in keyword_responses.items():
        if keyword in message_text:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
            break  # Salir del bucle después de encontrar la primera palabra clave

if __name__ == '__main__':
    application = ApplicationBuilder().token('7778816934:AAECQXKBpbWgVC-_lz53BFpp8lht4nWWoPY').build()  # Reemplaza con tu token

    # Manejador para el comando /start
    start_handler = CommandHandler('start', start)
    
    # Manejador para los mensajes que contengan las palabras clave
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), respond_to_keywords)

    # Añadir los manejadores a la aplicación
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    # Iniciar el bot
    application.run_polling()
