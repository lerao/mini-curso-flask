**Módulo 5: APIs REST, SOAP e Endpoints**

Neste módulo, os alunos aprenderão sobre APIs REST e Endpoints, incluindo:

* **APIs REST**
* **Endpoints**

**APIs REST**

As APIs REST (Representational State Transfer) são um padrão de arquitetura de software para APIs que usa o protocolo HTTP. As APIs REST são baseadas em recursos, que são entidades que podem ser acessadas por meio de URLs.

Para acessar um recurso, o cliente envia uma solicitação HTTP para a URL do recurso. A solicitação HTTP especifica o tipo de operação que o cliente deseja realizar, como GET, POST, PUT ou DELETE.

O servidor responde à solicitação com uma resposta HTTP. A resposta HTTP contém a representação do estado do recurso.

**APIs SOAP**

Para ciência, existe um outro tipo de APIs, que são as SOAP (Simple Object Access Protocol). Elas são um padrão de arquitetura de software para APIs que usa o protocolo SOAP. As APIs SOAP são baseadas em mensagens, que são trocadas entre o cliente e o servidor. As mensagens SOAP são XML-encapsuladas e contêm informações sobre o método a ser chamado, os parâmetros da chamada e os dados de retorno.

**Endpoints**

Os endpoints são pontos de extremidade de uma API. Um endpoint é uma URL que pode ser usada para acessar um recurso ou serviço.

Os endpoints são uma parte importante das APIs REST e SOAP. Eles permitem que os clientes acessem os recursos e serviços de uma API de forma consistente e uniforme.

**Exemplos**

Uma API REST para um serviço de previsão do tempo.

```python
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
```