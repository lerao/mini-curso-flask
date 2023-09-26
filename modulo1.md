**Módulo 1: Introdução a Flask**

Este módulo introduz os fundamentos do framework web Flask. Os tópicos abordados incluem:

* **Instalação e configuração:** Flask é um framework web de código aberto, gratuito e leve escrito em Python. Para instalar o Flask, basta usar o gerenciador de pacotes Python pip:

```
pip install flask
```

Depois de instalar o Flask, você pode criar um novo aplicativo Flask usando a função `Flask()`:

```python
from flask import Flask

app = Flask(__name__)
```

A função `Flask()` recebe um nome como parâmetro. O nome é usado para identificar o aplicativo e evitar conflitos com outros aplicativos Flask.

* **Rotinas de inicialização:** As rotinas de inicialização são funções que são chamadas quando o aplicativo Flask é iniciado. Essas funções podem ser usadas para configurar o aplicativo, carregar dados ou realizar outras tarefas que precisam ser executadas antes que o aplicativo comece a atender solicitações.

Para criar uma rotina de inicialização, basta adicionar uma função à lista de importações do aplicativo:

```python
from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request():
  print("This is the before_first_request function")
```

* **Rotas e Views:** Rotas são as URLs que o aplicativo Flask responde. Views são as funções que são chamadas quando uma solicitação é feita para uma determinada rota.

Para criar uma rota, basta usar a função `route()`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  # This function will be called when the request is made to the / URL

  return "Hello, World!"
```

* **Ambientes:** Os ambientes são uma maneira de configurar as configurações do aplicativo Flask para diferentes ambientes, como desenvolvimento, teste e produção.

Para definir um ambiente, basta definir a variável de ambiente `FLASK_ENV`:

```
export FLASK_ENV=development
```

Este ambiente define as configurações do aplicativo para o ambiente de desenvolvimento. Para obter mais informações sobre ambientes, consulte a documentação do Flask. Por ora, não vamos precisar alterar.

Documentação do Flask: https://flask.palletsprojects.com/en/2.3.x/

**Como funciona uma API REST**

Uma API REST (Representational State Transfer) é um padrão de arquitetura de software para APIs que usa o protocolo HTTP. As APIs REST são baseadas em recursos, que são entidades que podem ser acessadas por meio de URLs.

Para acessar um recurso, o cliente envia uma solicitação HTTP para a URL do recurso. A solicitação HTTP especifica o tipo de operação que o cliente deseja realizar, como GET, POST, PUT ou DELETE.

O servidor responde à solicitação com uma resposta HTTP. A resposta HTTP contém a representação do estado do recurso.

**Códigos de erros**

As APIs REST usam códigos de status HTTP para indicar o sucesso ou o fracasso de uma solicitação. Os códigos de status HTTP mais comuns são:

* **200 OK:** A solicitação foi bem-sucedida.
* **400 Bad Request:** A solicitação está incorreta.
* **401 Unauthorized:** O cliente não está autorizado a acessar o recurso.
* **403 Forbidden:** O cliente não tem permissão para acessar o recurso.
* **404 Not Found:** O recurso não foi encontrado.
* **500 Internal Server Error:** O servidor encontrou um erro interno.

**Consulta com GET/POST/PUT/DELETE**

As APIs REST usam os métodos HTTP GET, POST, PUT e DELETE para realizar operações em recursos.

* **GET:** O método GET é usado para recuperar um recurso.
* **POST:** O método POST é usado para criar um novo recurso.
* **PUT:** O método PUT é usado para atualizar um recurso existente.
* **DELETE:** O método DELETE é usado para excluir um recurso existente.

**Exemplos**

Aqui estão alguns exemplos de como usar as APIs REST:

* **GET /users:** Esta solicitação retornará uma lista de todos os usuários.
* **POST /users:** Esta solicitação criará um novo usuário.
* **PUT /users/1234:** Esta solicitação atualizará o usuário com o ID 1234.
* **DELETE /users/1234:** Esta solicitação excluirá o usuário com o ID 1234.

Para obter mais informações sobre APIs REST, consulte a documentação da RFC 2616.

RFC 2616: https://datatracker.ietf.org/doc/html/rfc2616
Resumo: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status

