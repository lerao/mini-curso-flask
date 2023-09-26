**Módulo 0: Introdução à Python**

Este módulo introduz os conceitos básicos da linguagem de programação Python. Os tópicos abordados incluem:

* **Hello World:** O programa Hello World é um programa simples que imprime a mensagem "Hello, World!" na tela.
* **Tipos de dados:** Python suporta os seguintes tipos de dados: int, float, str, bool, tuple, list e dict.
* **Estruturas de controle:** Python suporta as seguintes estruturas de controle: if, elif, else, for, while, try, except.
* **List comprehension:** A list comprehension é uma forma concisa de criar listas.
* **Funções:** As funções são blocos de código que podem ser reutilizados.
* **Classes:** As classes são um modo de organizar o código e criar objetos.
* **Database (sqlite):** SQLite é um banco de dados relacional embutido em Python.
* **Database with SQLAlchemy:** SQLAlchemy é um ORM (Object Relational Mapper) que permite trabalhar com bancos de dados relacionais em Python.

**Exemplos:**

* Hello World:

```python
print("Hello, World!")
```

* Tipos de dados:

```python
int = 10
float = 10.5
str = "Hello, World!"
bool = True
tuple = (1, 2, 3)
list = [1, 2, 3]
dict = {"key1": "value1", "key2": "value2"}
```

* Estruturas de controle:

```python
if x > 0:
  print("x é positivo")
elif x == 0:
  print("x é zero")
else:
  print("x é negativo")

for i in range(10):
  print(i)

while x < 10:
  print(x)
  x += 1
```

* List comprehension:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)
```

* Try, Except:

```python
try:
  x = int(input("Digite um número: "))
except ValueError:
  print("O valor digitado não é um número")
```

* Funções:

```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
```

* Classes:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_hello(self):
    print("Hello, my name is {} and I am {} years old".format(self.name, self.age))

person = Person("Bard", 10)
person.say_hello()
```

* Database (sqlite):

```python
import sqlite3

conn = sqlite3.connect("mydatabase.db")

c = conn.cursor()

c.execute("CREATE TABLE people (name TEXT, age INTEGER)")

c.execute("INSERT INTO people (name, age) VALUES ('Bard', 10)")

conn.commit()

conn.close()
```

(Inserir declaração de objetos, herança com Python)


* Database with SQLAlchemy:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mydatabase.db")

Session = sessionmaker(bind=engine)

session = Session()

person = Person(name="Bard", age=10)

session.add(person)

session.commit()

session.close()
```

Este é apenas um breve resumo dos tópicos abordados no Módulo 0. Para mais informações, consulte a documentação oficial do Python.

https://docs.python.org/3/