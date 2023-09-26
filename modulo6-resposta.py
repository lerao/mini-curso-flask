from flask import Flask, request, render_template, redirect, url_for, session
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
app.secret_key = 'sua_chave_secreta_aqui'

# Dados fictícios de usuários (neste exemplo, armazenados em um dicionário)
users = {
  'user1': 'password1',
  'user2': 'password2',
}

# Função para verificar se o usuário existe
@auth.verify_password
def verify_password(username, password):
  if username in users and users[username] == password:
    return username

# Rota de login
@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if verify_password(username, password):
      session['username'] = username
      return redirect(url_for('secreto'))
  
  return render_template('login.html')

# Rota protegida por autenticação
@app.route('/secreto')
@auth.login_required
def secreto():
  return render_template('secreto.html')

if __name__ == '__main__':
  app.run(debug=True)