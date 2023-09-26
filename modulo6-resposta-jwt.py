from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
jwt = JWTManager(app)

# Dados fictícios de usuários (neste exemplo, armazenados em um dicionário)
users = {
  'user1': 'password1',
  'user2': 'password2',
}

# Rota de login que gera um token JWT
# Use uma aplicação como o POSTMan para poder testar as rotas
@app.route('/', methods=['POST'])
def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')

  if username in users and users[username] == password:
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

  return jsonify(message='Login inválido'), 401

# Rota protegida por autenticação JWT
@app.route('/secreto')
@jwt_required()
def secreto():
  current_user = get_jwt_identity()
  return render_template('login.html', username=current_user)

if __name__ == '__main__':
  app.run(debug=True)