```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/user/<username>')
def hello_user(username):
    return "Hello, {}!".format(username)

@app.route('/page/<int:page_number>')
def list_pages(page_number):
    # Suponhamos que você queira retornar uma lista de páginas como exemplo.
    # Você pode criar uma lista fictícia aqui.
    pages = [f'Page {i}' for i in range(1, page_number + 1)]
    return ", ".join(pages)

if __name__ == '__main__':
    app.run()
```