from flask import Flask, render_template, request, jsonify
from evaluator import evaluar_password
from generator import generar_contraseña
import os

app = Flask(__name__)

# Ruta principal: Sirve la página web
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/evaluator')
def evaluator():
    return render_template('evaluator.html')

@app.route('/storage')
def storage():
    return render_template('storage.html')

@app.route('/interface')
def interface():
    return render_template('interface.html')

# API: Evaluar contraseña
@app.route('/api/evaluar', methods=['POST'])
def api_evaluar():
    data = request.get_json()
    password = data.get('password', '')
    
    if not password:
        return jsonify({'error': 'No password provided'}), 400
        
    puntaje, es_comun, el_hash, entropia = evaluar_password(password)
    
    # Generar feedback basado en el puntaje
    feedback = ""
    if es_comun:
        feedback = "¡ALERTA! Esta contraseña es súper común. ¡Cámbiala ya!"
    elif puntaje < 40:
        feedback = "Mmm... está medio débil. Ponle más ganas."
    elif puntaje < 70:
        feedback = "Va mejorando, pero puede estar más chida."
    else:
        feedback = "¡Eso es! Una contraseña digna de un pro."
        
    return jsonify({
        'puntaje': puntaje,
        'es_comun': es_comun,
        'entropia': round(entropia, 2),
        'feedback': feedback
    })

# API: Generar contraseña
@app.route('/api/generar', methods=['GET'])
def api_generar():
    password = generar_contraseña()
    return jsonify({'password': password})

if __name__ == '__main__':
    # Escuchar en todas las interfaces para facilitar pruebas
    app.run(debug=True, host='0.0.0.0', port=5000)
