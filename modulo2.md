**Módulo 2: Rotas e views**

**Rotas estáticas**

As rotas estáticas são aquelas que correspondem a URLs que não contêm nenhum parâmetro. Por exemplo, a rota `/` corresponde à URL `/`.

Para criar uma rota estática, basta usar a função `route()`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  # Esta rota corresponde à URL /

  return "Hello, World!"
```

Quando um usuário faz uma solicitação para a URL `/`, a view `index()` é chamada.

**Rotas dinâmicas**

As rotas dinâmicas são aquelas que correspondem a URLs que contêm parâmetros. Os parâmetros são usados para passar informações para a view.

Para criar uma rota dinâmica, basta usar a função `route()` com um parâmetro:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
  # Esta rota corresponde à URL /user/<username>

  return "Hello, {}!".format(username)
```

Quando um usuário faz uma solicitação para a URL `/user/teste`, a view `user()` é chamada e o parâmetro `username` é passado com o valor `teste`.

**Parâmetros de rota**

Os parâmetros de rota são parâmetros que são passados para a view por meio da URL. Os parâmetros de rota são especificados entre colchetes angulares (`<>`) na função `route()`.

Os parâmetros de rota podem ser usados para recuperar informações do usuário ou para controlar o comportamento da view.

**Parâmetros de consulta**

Os parâmetros de consulta são parâmetros que são passados para a view por meio da consulta da URL. Os parâmetros de consulta são especificados após o sinal de interrogação (`?`) na URL.

Os parâmetros de consulta podem ser usados para recuperar informações do usuário ou para controlar o comportamento da view.

**Exemplos**

Aqui estão alguns exemplos de como usar rotas estáticas e dinâmicas:

* **Rotas estáticas:**
    * `/`: Esta rota corresponde à URL `/`.
    * `/about`: Esta rota corresponde à URL `/about`.
    * `/contact`: Esta rota corresponde à URL `/contact`.
* **Rotas dinâmicas:**
    * `/user/<username>`: Esta rota corresponde à URL `/user/<username>`, onde `<username>` é um parâmetro de rota.
    * `/page/<page_number>`: Esta rota corresponde à URL `/page/<page_number>`, onde `<page_number>` é um parâmetro de rota.
    * `/search?q=<query>`: Esta rota corresponde à URL `/search?q=<query>`, onde `<query>` é um parâmetro de consulta.

**Exercícios**

* Crie um aplicativo Flask com as seguintes rotas:
    * `/`: Esta rota deve retornar a mensagem "Hello, World!".
    * `/user/<username>`: Esta rota deve retornar a mensagem "Hello, {}!", onde `<username>` é um parâmetro de rota.
    * `/page/<page_number>`: Esta rota deve retornar uma lista de páginas, onde `<page_number>` é um parâmetro de consulta.

**Próximo módulo**

No próximo módulo, veremos como trabalhar com modelos de dados em Flask.