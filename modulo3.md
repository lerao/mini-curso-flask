**Módulo 3: Modelos de dados**

Neste módulo,  vamos mostrar como trabalhar com modelos de dados em Flask, incluindo:

* Modelos de dados
* Bancos de dados
* ORMs

**Modelos de dados**

Os modelos de dados são classes que representam dados em um aplicativo Flask. Os modelos de dados são usados para armazenar dados, recuperar dados e manipular dados.

Para criar um modelo de dados, basta criar uma classe que herda da classe `db.Model` do SQLAlchemy:

```python
from sqlalchemy import Column, Integer, String

class User(db.Model):
  id = Column(Integer, primary_key=True)
  username = Column(String(255))
```

Esta classe representa um usuário. A classe tem duas colunas:

* `id`: Este é o ID do usuário.
* `username`: Este é o nome de usuário do usuário.

**Bancos de dados**

Os bancos de dados são usados para armazenar dados em um aplicativo Flask. Flask suporta uma variedade de bancos de dados, incluindo MySQL, PostgreSQL e SQLite.

Para usar um banco de dados em um aplicativo Flask, basta criar uma conexão com o banco de dados usando a classe `db.engine()`:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydatabase.db")
```

Esta conexão é usada para acessar o banco de dados.

**ORMs**

Os ORMs (Object Relational Mappers) são ferramentas que ajudam a mapear modelos de dados para tabelas de banco de dados. Flask suporta o SQLAlchemy, um ORM popular.

Para usar o SQLAlchemy em um aplicativo Flask, basta importar o SQLAlchemy e criar uma instância do `Session()`:

```python
from sqlalchemy import create_engine, Session

engine = create_engine("sqlite:///mydatabase.db")
session = Session(engine)
```

Esta instância é usada para interagir com o banco de dados.

**Exemplos**

Aqui estão alguns exemplos de como usar modelos de dados em Flask:

* **Criando um novo usuário:**

```python
user = User(username="teste")
session.add(user)
session.commit()
```

Estas linhas de código criam um novo usuário com o nome de usuário "teste".

* **Recuperando um usuário:**

```python
user = session.query(User).filter_by(username="teste").first()
```

Estas linhas de código recuperam o usuário com o nome de usuário "teste".

* **Atualizando um usuário:**

```python
user.username = "teste2"
session.commit()
```

Estas linhas de código atualizam o nome de usuário do usuário para "teste2".

* **Excluindo um usuário:**

```python
session.delete(user)
session.commit()
```

Estas linhas de código excluem o usuário.

**Exercícios**

* Crie um aplicativo Flask com um modelo de dados para representar um usuário.
* Crie uma rota que permita ao usuário criar uma nova conta.
* Crie uma rota que permita ao usuário visualizar seu perfil.
* Teste as rotas criadas nos exercícios anteriores.

**Próximo módulo**

No próximo módulo, vamos trabalhar com formulários em Flask.