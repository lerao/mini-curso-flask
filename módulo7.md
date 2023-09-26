**Módulo 7: Testes em Flask**

Neste módulo, os alunos aprenderão sobre testes em Flask, incluindo:

* **Testes unitários**
* **Testes de integração**
* **Testes de aceitação**

**Testes unitários**

Testes unitários são testes que testam unidades individuais de código, como funções ou métodos. Testes unitários são importantes para garantir que o código funcione conforme o esperado.

Para escrever testes unitários em Flask, podemos usar o módulo `unittest` do Python. O módulo `unittest` fornece uma variedade de ferramentas que podem ser usadas para escrever testes unitários.

**Testes de integração**

Testes de integração são testes que testam a interação entre unidades individuais de código. Testes de integração são importantes para garantir que as unidades individuais de código funcionem juntas conforme o esperado.

Para escrever testes de integração em Flask, podemos usar o módulo `unittest` do Python ou o módulo `flask_testing`. O módulo `flask_testing` fornece uma variedade de ferramentas que podem ser usadas para escrever testes de integração.

**Testes de aceitação**

Testes de aceitação são testes que testam o comportamento do aplicativo como um todo. Testes de aceitação são importantes para garantir que o aplicativo atenda aos requisitos dos usuários.

Para escrever testes de aceitação em Flask, podemos usar o módulo `unittest` do Python ou um framework de testes de aceitação, como o `behave`.

**Exemplos**

Aqui estão alguns exemplos de como escrever testes em Flask:

* **Teste de unidade para uma função que calcula o comprimento de uma string:**

```python
def test_len(self):
    self.assertEqual(len("Hello, world!"), 13)
```

* **Teste de integração para uma rota que retorna uma lista de usuários:**

```python
def test_users_list(self):
    client = app.test_client()
    response = client.get("/users")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), [{"id": 1, "username": "bard"}, {"id": 2, "username": "user2"}])
```

* **Teste de aceitação para um aplicativo de e-commerce:**

```python
def test_add_product_to_cart(self):
    client = app.test_client()
    response = client.post("/products/1/add-to-cart")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), {"success": True})
```

**Exercícios**

* Escreva testes unitários para uma função que calcula o comprimento de uma string.