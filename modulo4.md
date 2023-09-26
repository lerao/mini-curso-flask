**Módulo 4: Formulários**

Neste módulo, vamos aprender como trabalhar com formulários em Flask, incluindo:

* Criando formulários
* Validando formulários
* Enviando formulários

**Criando formulários**

Os formulários são usados para coletar dados do usuário. Flask fornece uma biblioteca de formulários embutida que pode ser usada para criar formulários facilmente.

```python
pip install Flask-WTF
```

Para criar um formulário, basta importar a biblioteca de formulários e criar um objeto `Form()`:

```python
@app.route("/")
def index():
  form = Form()
  return render_template("index.html", form=form)
```

Estas linhas de código criam um formulário com um campo de texto.

**Validando formulários**

Flask fornece um conjunto de validadores embutidos que podem ser usados para verificar os dados do formulário. Para validar um formulário, basta chamar o método `validate()` no objeto `Form()`:

```python
@app.route("/")
def index():
  form = Form()

  if form.validate_on_submit():
    print(form.username.data)
  else:
    print(form.errors)

  return render_template("index.html", form=form)
```

Estas linhas de código verificam o campo de texto do formulário. Se o campo de texto estiver vazio, o formulário não será válido.

**Enviando formulários**

Os dados do formulário podem ser enviados para o servidor usando o método `post()`:

```python
@app.route("/")
def index():
  form = Form()

  if form.validate_on_submit():
    username = form.username.data
    print("O nome de usuário é:", username)

  return render_template("index.html", form=form)
```

Estas linhas de código enviam os dados do formulário para o servidor.

**Exemplos**

Aqui estão alguns exemplos de como usar formulários em Flask:

* **Um formulário de login:**

```python
@app.route("/")
def index():
  form = Form()

  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data

    if username == "teste" and password == "secret":
      return "Login bem-sucedido!"
    else:
      return "Usuário ou senha inválidos."

  return render_template("index.html", form=form)
```

Este formulário permite ao usuário fazer login no aplicativo.

* **Um formulário de contato:**

```python
@app.route("/")
def index():
  form = Form()

  if form.validate_on_submit():
    name = form.name.data
    email = form.email.data
    message = form.message.data

    print(f"Nome: {name}")
    print(f"E-mail: {email}")
    print(f"Mensagem: {message}")

  return render_template("index.html", form=form)
```

Este formulário permite ao usuário enviar uma mensagem de contato.

**Exercícios**

* Crie um aplicativo Flask com um formulário de login.
* Crie um aplicativo Flask com um formulário de contato.
* Teste os formulários criados nos exercícios anteriores.

**Próximo módulo**

No próximo módulo, os alunos aprenderão como trabalhar com autenticação e autorização em Flask.