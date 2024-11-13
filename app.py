from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    expresion = data.get('expresion', '')
    try:
        # Evalúa la expresión de manera segura
        resultado = eval(expresion)
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'resultado': 'Error'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
