import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Periksa konfigurasi API key dengan cara yang lebih aman
genai.configure(api_key= "AIzaSyAv5YmcpdWtw-9CE5B1SnlalMJ0igHV8Wg")  # Menyimpan key di environment variabel

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Anda bisa mengganti model_name jika menggunakan model yang lebih spesifik atau sesuai
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Periksa nama model yang sesuai dengan dokumentasi terbaru
    generation_config=generation_config,
)

app = Flask(__name__)

def GeneratedResponse(input_text):
    # Menyusun prompt dengan cara yang benar
    response = model.generate_content([
        "Kamu adalah seseorang yang bernama BOTO, kamu merupakan pemandu pariwisata di Sumatera Utara, "
        "kamu mengetahui tempat wisata dan tempat penginapan di Sumatera Utara serta beri alamat tempatnya "
        "dan link Google Map tempat wisata dan penginapan. Kamu juga dapat menjawab pertanyaan yang bersangkutan "
        "dengan pernyataanmu sebelumnya. Kamu tahu cafe yang ada di Sumatera Utara. ",
        f"User  : {input_text}",
        "Si Boto   : ",
    ])
    
    return response.text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = GeneratedResponse(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
 