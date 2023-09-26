**Módulo 6: Autenticação e autorização em APIs REST**

Neste módulo, os alunos aprenderão sobre autenticação e autorização em APIs REST, incluindo:

* **Autenticação**
* **Autorização**
* **OAuth**
* **JWT**

**Autenticação**

A autenticação é o processo de verificar a identidade de um usuário. A autenticação é necessária para proteger APIs de acesso não autorizado.

Existem vários métodos de autenticação que podem ser usados em APIs, incluindo:

* **Nome de usuário e senha:** Este é o método de autenticação mais comum. Os usuários fornecem um nome de usuário e senha para autenticar.
* **Tokens:** Os tokens são pequenos pedaços de dados que podem ser usados para autenticar usuários. Os tokens são gerados pelo servidor e enviados para o cliente.
* **Certificados digitais:** Os certificados digitais são usados para autenticar usuários e proteger as comunicações.

**Autorização**

A autorização é o processo de conceder acesso a um recurso ou serviço. A autorização é necessária para controlar o acesso de usuários a recursos e serviços específicos.

Existem vários métodos de autorização que podem ser usados em APIs, incluindo:

* **Roles:** Os usuários são atribuídos a funções ou roles. Os papéis determinam quais recursos e serviços os usuários podem acessar.
* **Permissões:** As permissões são concedidas a usuários ou papéis. As permissões determinam quais operações os usuários podem realizar em recursos e serviços.

**OAuth**

OAuth é um protocolo de autorização aberto que permite que os usuários autorizem aplicativos a acessar seus dados sem compartilhar suas senhas.

OAuth funciona usando um fluxo de autorização de quatro etapas:

1. O cliente solicita autorização do usuário.
2. O servidor de autorização solicita consentimento do usuário.
3. O usuário concede consentimento ao servidor de autorização.
4. O servidor de autorização emite um token de acesso ao cliente.

**JWT**

JWT (JSON Web Token) é um formato de token de acesso leve e seguro baseado em JSON. JWTs são usados para transmitir informações de autenticação e autorização entre partes.

JWTs são compostos de três partes:

* **Cabeçalho:** O cabeçalho contém informações sobre o token, como o tipo de token e o algoritmo de assinatura.
* **Corpo:** O corpo contém as informações de autenticação e autorização, como o nome de usuário, o papel e o tempo de expiração do token.
* **Assinatura:** A assinatura é usada para verificar a integridade do token.

**Exemplos**

Aqui estão alguns exemplos de como autenticar e autorizar usuários em APIs REST:

* **API REST de um serviço de e-commerce:** O usuário pode se autenticar com seu nome de usuário e senha. Depois de autenticado, o usuário pode acessar recursos e serviços, como comprar produtos, adicionar produtos ao carrinho de compras e fazer checkout.

**Exercícios**

* Implemente autenticação e autorização em uma API REST usando o método de autenticação de nome de usuário e senha.
* Implemente autenticação e autorização em uma API REST usando o método de autenticação com JWT (pip install Flask-JWT-Extended);
* Teste as implementações de autenticação e autorização criadas nos exercícios anteriores.

**Próximo módulo**

No próximo módulo, vamos aprender sobre testes em Flask.