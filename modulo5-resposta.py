from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de dados de previsão do tempo
weather_data = {
    'city1': {'temperature': 25, 'condition': 'Sunny'},
    'city2': {'temperature': 15, 'condition': 'Cloudy'},
}

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)