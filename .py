import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai


genai.configure(api_key="AIzaSyAv5YmcpdWtw-9CE5B1SnlalMJ0igHV8Wg")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  
    generation_config=generation_config,
)


app = Flask(__name__)


def GeneratedResponse(input_text):
    
    response = model.generate_content([
        "Kamu adalah seseorang yang bernama BOTO, kamu merupakan pemandu pariwisata di Sumatera Utara. "
        "Jawablah dalam bentuk poin-poin. Untuk setiap tempat wisata atau penginapan, beri nama, alamat, "
        "dan link Google Map-nya.",
        f"User  : {input_text}",
        "Si Boto   : ",
    ])
    
    response_text = response.text.strip()
    response_list = response_text.split('\n') 
    return response_list


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response_list = GeneratedResponse(user_input) 
    return jsonify({'response': bot_response_list})


if __name__ == '__main__':
    app.run(debug=True)
