from flask import Flask, request, jsonify
from utils.openai_utils import process_text
from utils.whisper_utils import transcribe_audio
from utils.vision_utils import analyze_image
from utils.twilio_utils import send_whatsapp_message
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Configurar credenciais do Google Cloud Vision
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if credentials_path:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
else:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS não definida no .env")

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    msg_type = data.get('type')
    content = data.get('content')
    sender = data.get('from')

    response = "Desculpe, não entendi sua mensagem."

    try:
        if msg_type == 'text':
            response = process_text(content)
        elif msg_type == 'audio':
            text = transcribe_audio(content)
            response = process_text(text)
        elif msg_type == 'image':
            result = analyze_image(content)
            if result:
                response = result
            else:
                response = "Não encontramos o item. Irei agendar um atendimento com especialista."
        
        # Enviar a resposta via WhatsApp
        send_whatsapp_message(sender, response)

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
