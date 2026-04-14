import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from google import genai
from datetime import datetime
import os

# --- CONFIGURACIÓN ---
TOKEN_TELEGRAM = '8615261340:AAEWxzIdmvZ6kIKptFuBxex550Y5ohgCytc' 
LLAVE_GEMINI = 'AIzaSyBzMus71nwFk1D54cI3bme4pdXt_auigWY'

# ⚠️ ID de Telegram para recibir capturas (obténido con @userinfobot)
TU_ID_TELEGRAM = 6044120816

# Inicialización
client = genai.Client(api_key=LLAVE_GEMINI)
bot = telebot.TeleBot(TOKEN_TELEGRAM)

# --- VARIABLES PARA OFRENDAS ---
estado_ofrenda = {}

# --- MENÚ PRINCIPAL ---
@bot.message_handler(commands=['start'])
def enviar_bienvenida(message):
    user_name = message.from_user.first_name
    
    bot.send_message(
        message.chat.id,
        f"🙏 Bendiciones ¡Bienvenido(a) al Asistente Virtual Roca Fuerte, {user_name}!\n\n"
        f"✨ Estoy aquí para servirte, ayudarte y bendecirte.\n"
        f"¿En qué puedo ayudarte hoy?",
        parse_mode="Markdown"
    )
    
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("📅 Horarios", callback_data="horarios"),
        InlineKeyboardButton("💰 Ofrendas", callback_data="p"),
        InlineKeyboardButton("📍 Ubicación", callback_data="u"),
        InlineKeyboardButton("📺 YouTube", url="https://www.youtube.com/@RocaFuerteInternacional"),
        InlineKeyboardButton("❓ Ayuda", callback_data="ayuda")
    )
    
    bot.send_message(
        message.chat.id,
        "📋 Selecciona una opción:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# --- MANEJADOR PRINCIPAL DE BOTONES ---
@bot.callback_query_handler(func=lambda call: True)
def manejar_botones(call):
    # Submenú de Horarios
    if call.data == "horarios":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("🙏 Servicio Familiar", callback_data="hfamiliar"),
            InlineKeyboardButton("🔥 Servicio Jóvenes", callback_data="hjovenes"),
            InlineKeyboardButton("🌅 Matutinos (5AM)", callback_data="hmatutinos"),
            InlineKeyboardButton("🕊️ Servicio Descanso", callback_data="hdescanso"),
            InlineKeyboardButton("📢 Eventos/Anuncios", callback_data="heventos"),
            InlineKeyboardButton("🔙 Volver", callback_data="volver")
        )
        
        bot.send_message(
            call.message.chat.id,
            "📅 Selecciona un horario:",
            parse_mode="Markdown",
            reply_markup=markup
        )
    
    # Servicio Familiar (Domingo)
    elif call.data == "hfamiliar":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver a Horarios", callback_data="horarios"))
        
        if os.path.exists("familiar.jpg"):
            with open("familiar.jpg", "rb") as foto:
                bot.send_photo(
                    call.message.chat.id,
                    foto,
                    caption="""🙏 SERVICIO FAMILIAR

📅 Domingo - 8:00 AM

🚌 Transporte disponible:
* Salida: 7:30 AM
* Danto y Ojeda

✨ ¡Toda la familia es bienvenida!

\"Bienaventurados los que habitan en tu casa\" (Salmo 84:4)""",
                    reply_markup=markup
                )
        else:
            bot.send_message(
                call.message.chat.id,
                """🙏 SERVICIO FAMILIAR

📅 Domingo - 8:00 AM

🚌 Transporte disponible:
* Salida: 7:30 AM
* Danto y Ojeda

✨ ¡Toda la familia es bienvenida!

\"Bienaventurados los que habitan en tu casa\" (Salmo 84:4)""",
                parse_mode="Markdown",
                reply_markup=markup
            )
    
    # Servicio Jóvenes (Viernes)
    elif call.data == "hjovenes":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver a Horarios", callback_data="horarios"))
        
        if os.path.exists("jovenes.jpg"):
            with open("jovenes.jpg", "rb") as foto:
                bot.send_photo(
                    call.message.chat.id,
                    foto,
                    caption="""🔥 SERVICIO DE JÓVENES

📅 Viernes - 5:00 PM

🚌 Transporte disponible:
* Salida: 4:30 PM
* Danto y Ojeda

\"UN NUEVO MES... pero el mismo DIOS\" ✝️

🎸 ¡Te esperamos para adorar juntos!""",
                    reply_markup=markup
                )
        else:
            bot.send_message(
                call.message.chat.id,
                """🔥 SERVICIO DE JÓVENES

📅 Viernes - 5:00 PM

🚌 Transporte disponible:
* Salida: 4:30 PM
* Danto y Ojeda

\"UN NUEVO MES... pero el mismo DIOS\" ✝️

🎸 ¡Te esperamos para adorar juntos!""",
                parse_mode="Markdown",
                reply_markup=markup
            )
    
    # Matutinos (Lunes a Viernes 5AM)
    elif call.data == "hmatutinos":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver a Horarios", callback_data="horarios"))
        
        if os.path.exists("matutinos.jpg"):
            with open("matutinos.jpg", "rb") as foto:
                bot.send_photo(
                    call.message.chat.id,
                    foto,
                    caption="""🌅 MATUTINOS - ENCUENTRO CON DIOS

📅 Lunes a Viernes - 5:00 AM

💻 Únete por Zoom:
🔗 [Haz clic aquí para unirte](https://us06web.zoom.us/j/87361492135?pwd=yVbWeGeoKK8fJ0Ha7DnihUGxDSstIX.1)

📌 ID: 873 6149 2135
🔑 Código: Roca

\"Temprano yo te buscaré\" (Salmo 63:1)""",
                    reply_markup=markup
                )
        else:
            bot.send_message(
                call.message.chat.id,
                """🌅 MATUTINOS - ENCUENTRO CON DIOS

📅 Lunes a Viernes - 5:00 AM

💻 Únete por Zoom:
🔗 [Haz clic aquí para unirte](https://us06web.zoom.us/j/87361492135?pwd=yVbWeGeoKK8fJ0Ha7DnihUGxDSstIX.1)

📌 ID: 873 6149 2135
🔑 Código: Roca

\"Temprano yo te buscaré\" (Salmo 63:1)""",
                parse_mode="Markdown",
                reply_markup=markup
            )
    
    # Servicio de Descanso (Martes)
    elif call.data == "hdescanso":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver a Horarios", callback_data="horarios"))
        
        if os.path.exists("descanso.jpg"):
            with open("descanso.jpg", "rb") as foto:
                bot.send_photo(
                    call.message.chat.id,
                    foto,
                    caption="""🕊️ SERVICIO DE DESCANSO

📅 Martes - 6:30 PM
📍 Lugar: Auditorio Roca Fuerte

\"Venid a mí todos los que estáis trabajados y cargados, y yo os haré descansar\" (Mateo 11:28)

🙏 Descansamos a través de la oración""",
                    reply_markup=markup
                )
        else:
            bot.send_message(
                call.message.chat.id,
                """🕊️ SERVICIO DE DESCANSO

📅 Martes - 6:30 PM
📍 Lugar: Auditorio Roca Fuerte

\"Venid a mí todos los que estáis trabajados y cargados, y yo os haré descansar\" (Mateo 11:28)

🙏 Descansamos a través de la oración""",
                parse_mode="Markdown",
                reply_markup=markup
            )
    
    # Eventos/Anuncios
    elif call.data == "heventos":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver a Horarios", callback_data="horarios"))
        
        bot.send_message(
            call.message.chat.id,
            """📢 EVENTOS Y ANUNCIOS

✨ Próximamente...

Estamos preparando nuevas actividades para bendecir tu vida.

📌 Pronto anunciaremos:
* Eventos especiales
* Ventas y profundos
* Actividades para toda la familia

🙏 Mantente atento a este espacio

\"El Señor hará cosas grandes\" (Salmo 126:3)""",
            parse_mode="Markdown",
            reply_markup=markup
        )
    
    # Ubicación interactiva
    elif call.data == "u":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver al Menú", callback_data="volver"))
        
        bot.send_location(
            call.message.chat.id,
            latitude=10.189621,
            longitude=-71.297732
        )
        
        bot.send_message(
            call.message.chat.id,
            "📍 Iglesia Roca Fuerte\n"
            "Av. 34, Ciudad Ojeda 4019, Zulia\n\n"
            "¡Presiona el mapa para llegar!\n"
            "Te esperamos con los brazos abiertos. 🙏🏛️",
            parse_mode="Markdown",
            reply_markup=markup
        )
    
    # Ayuda
    elif call.data == "ayuda":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Volver al Menú", callback_data="volver"))
        
        bot.send_message(
            call.message.chat.id,
            "🙏 ¿En qué puedo ayudarte?\n\n"
            "✅ Puedo responder:\n"
            "• Preguntas bíblicas\n"
            "• Temas de fe y oración\n"
            "• Horarios de culto\n"
            "• Ofrendas y donaciones\n"
            "• Ubicación de la iglesia\n\n"
            "❌ NO puedo responder:\n"
            "• Temas políticos o deportivos\n"
            "• Recetas, películas, juegos\n"
            "• Noticias del mundo\n\n"
            "✨ Escríbeme tu pregunta espiritual!",
            parse_mode="Markdown",
            reply_markup=markup
        )
    
    # Submenú de Ofrendas
    elif call.data == "p":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("💰 Diezmo", callback_data="diezmo"),
            InlineKeyboardButton("💸 Ofrenda", callback_data="ofrenda"),
            InlineKeyboardButton("🙏 Voto", callback_data="voto"),
            InlineKeyboardButton("🌾 Primicias", callback_data="primicia"),
            InlineKeyboardButton("🔙 Volver", callback_data="volver")
        )
        
        bot.send_message(
            call.message.chat.id,
            "🙏 Selecciona el tipo de ofrenda:\n\n"
            "• Diezmo: El 10% de tus ingresos\n"
            "• Ofrenda: Donación voluntaria\n"
            "• Voto: Promesa a Dios\n"
            "• Primicias: Primeros frutos",
            parse_mode="Markdown",
            reply_markup=markup
        )
    
    # Volver al menú principal
    elif call.data == "volver":
        bot.answer_callback_query(call.id)
        
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("📅 Horarios", callback_data="horarios"),
            InlineKeyboardButton("💰 Ofrendas", callback_data="p"),
            InlineKeyboardButton("📍 Ubicación", callback_data="u"),
            InlineKeyboardButton("📺 YouTube", url="https://www.youtube.com/@RocaFuerteInternacional"),
            InlineKeyboardButton("❓ Ayuda", callback_data="ayuda")
        )
        bot.send_message(
            call.message.chat.id,
            "📋 Menú principal:",
            reply_markup=markup,
            parse_mode="Markdown"
        )
    
    # Tipos de ofrenda
    elif call.data in ["diezmo", "ofrenda", "voto", "primicia"]:
        iniciar_ofrenda(call)

# --- FLUJO DE OFRENDAS ---
def iniciar_ofrenda(call):
    tipo_ofrenda = {
        "diezmo": "DIEZMO",
        "ofrenda": "OFRENDA", 
        "voto": "VOTO",
        "primicia": "PRIMICIAS"
    }[call.data]
    
    bot.answer_callback_query(call.id)
    
    # Guardar estado
    estado_ofrenda[call.from_user.id] = {
        "tipo": tipo_ofrenda,
        "paso": "esperando_nombre"
    }
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Cancelar y Volver", callback_data="volver"))
    
    mensaje_pago = f"""🙏 {tipo_ofrenda} - Iglesia Roca Fuerte

━━━━━━━━━━━━━━━━━━━━━
💳 PAGO MÓVIL
━━━━━━━━━━━━━━━━━━━━━

🏦 Banco Mercantil
📱 04121712054
🪪 J307824255

Ministerio Internacional Roca Fuerte

━━━━━━━━━━━━━━━━━━━━━
📝 Escribe tu nombre para registrar tu ofrenda:"""

    bot.send_message(
        call.message.chat.id,
        mensaje_pago,
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.from_user.id in estado_ofrenda and estado_ofrenda[message.from_user.id]["paso"] == "esperando_nombre")
def recibir_nombre(message):
    nombre = message.text.strip()
    user_id = message.from_user.id
    
    estado_ofrenda[user_id]["nombre"] = nombre
    estado_ofrenda[user_id]["paso"] = "esperando_capture"
    
    bot.reply_to(
        message,
        f"🙏 Gracias {nombre}\n\n"
        f"Ahora envía el COMPROBANTE de tu {estado_ofrenda[user_id]['tipo']}.\n\n"
        f"📸 Adjunta la imagen aquí ↓",
        parse_mode="Markdown"
    )

@bot.message_handler(content_types=['photo'], func=lambda message: message.from_user.id in estado_ofrenda and estado_ofrenda[message.from_user.id]["paso"] == "esperando_capture")
def recibir_capture(message):
    user_id = message.from_user.id
    info = estado_ofrenda[user_id]
    nombre = info["nombre"]
    tipo = info["tipo"]
    
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    texto_notificacion = f"""🏛️ NUEVA OFRENDA - ROCA FUERTE

📌 Tipo: {tipo}
👤 De parte de: {nombre}
🕒 Fecha: {fecha}
📱 Usuario: @{message.from_user.username if message.from_user.username else message.from_user.first_name}

✅ Pendiente de verificación

📲 Enviar comprobante a: 04121712054"""
    
    try:
        bot.send_message(TU_ID_TELEGRAM, texto_notificacion, parse_mode="Markdown")
        bot.send_photo(TU_ID_TELEGRAM, message.photo[-1].file_id, caption=f"Comprobante - {tipo} - {nombre}")
        
        estado_ofrenda[user_id]["chat_id"] = user_id
        estado_ofrenda[user_id]["paso"] = "esperando_confirmacion"
        
        bot.reply_to(
            message,
            f"✅ ¡Recibido {nombre}!\n\n"
            f"Tu {tipo} ha sido registrado.\n"
            f"\"Dios ama al dador alegre\" (2 Corintios 9:7)\n\n"
            f"🙏 ¡Dios multiplique tu siembra!\n\n"
            f"📲 Nota: El equipo de administración confirmará tu aporte.",
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(
            message,
            "❌ Hubo un error. Por favor envía tu comprobante al WhatsApp 04121712054"
        )

# --- INTELIGENCIA ARTIFICIAL (LIMITADA) ---
@bot.message_handler(func=lambda message: True)
def consulta_ia(message):
    # Evitar que responda a mensajes del flujo de ofrendas
    if message.from_user.id in estado_ofrenda:
        return
    
    texto = message.text.lower().strip()
    
    # Palabras que NO debe responder
    temas_prohibidos = [
        "confirmar", "confirmación", "verificar",
        "política", "gobierno", "presidente", "maduro", "chavismo", "oposición",
        "deporte", "fútbol", "beisbol", "baloncesto", "futbol",
        "clima", "tiempo", "temperatura", "lluvia",
        "receta", "cocina", "comida", "pizza", "pastel",
        "película", "serie", "netflix", "disney", "marvel",
        "videojuego", "juego", "playstation", "xbox",
        "noticia", "actualidad", "suceso"
    ]
    
    if any(palabra in texto for palabra in temas_prohibidos):
        bot.reply_to(
            message,
            "🙏 Soy el asistente virtual de la Iglesia Roca Fuerte\n\n"
            "Estoy entrenada para ayudarte con:\n"
            "• 📖 Preguntas bíblicas\n"
            "• 🙌 Temas de fe y espiritualidad\n"
            "• 🕒 Horarios de culto\n"
            "• 💰 Ofrendas y donaciones\n"
            "• 📍 Ubicación de la iglesia\n\n"
            "No estoy entrenada para otros temas.\n\n"
            "¿En qué puedo ayudarte con tu vida espiritual? ✨",
            parse_mode="Markdown"
        )
        return
    
    try:
        prompt = f"""Eres el asistente virtual de la Iglesia Roca Fuerte (Venezuela, Ciudad Ojeda).
Tu función es SOLO responder preguntas sobre:
- La Biblia y su interpretación
- Versículos y enseñanzas cristianas
- Oración y vida espiritual
- Consejos basados en principios bíblicos
- La iglesia (horarios, ubicación, ofrendas)

Si la pregunta NO tiene relación con estos temas, responde amablemente:
"Lo siento, soy un asistente de la iglesia y solo puedo ayudarte con temas espirituales. ¿Te gustaría que hablemos de algún versículo o necesidad de oración?"

Pregunta del usuario: {message.text}

Responde de manera cálida, cristiana y breve (máximo 3 párrafos)."""
        
        modelos = ["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-flash-latest"]
        
        for modelo in modelos:
            try:
                response = client.models.generate_content(
                    model=modelo,
                    contents=prompt
                )
                bot.reply_to(message, response.text)
                return
            except:
                continue
        
        bot.reply_to(message, "Lo siento, estoy en mantenimiento. ¡Vuelve pronto!")
        
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "Hermano, un momento por favor. ¡Reintenta ahora!")

print("--- ¡ASISTENTE ROCA FUERTE ACTIVADO! ---")
bot.infinity_polling()